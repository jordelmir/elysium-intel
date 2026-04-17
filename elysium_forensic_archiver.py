import sqlite3, requests, os

def archive_all():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    archive_dir = "/home/ubuntu/elysium_vault/forensic_snapshots"
    os.makedirs(archive_dir, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    rows = cur.execute("SELECT id_caso, url FROM cases WHERE id_caso LIKE \"CR-2025-%\" AND contenido_completo IS NOT NULL").fetchall()
    
    print(f"⚖️ [FORENSIC-ARCHIVER] Iniciando preservación legal de {len(rows)} casos...")
    for id_caso, url in rows:
        snapshot_path = f"{archive_dir}/{id_caso}.html"
        if not os.path.exists(snapshot_path):
            try:
                resp = requests.get(url, timeout=10)
                with open(snapshot_path, "w") as f:
                    f.write(resp.text)
            except: pass
    conn.close()
    print("✅ Preservación de pruebas finalizada.")

if __name__ == "__main__":
    archive_all()
