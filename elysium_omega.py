import sqlite3, hashlib, datetime

def integrity_seal():
    # Sella el Vault para asegurar que nadie modifique el historial
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    data = conn.execute("SELECT * FROM cases ORDER BY id_caso").fetchall()
    seal = hashlib.sha256(str(data).encode()).hexdigest()
    conn.execute("INSERT OR REPLACE INTO external_factors (fecha, variable, valor, fuente) VALUES (?, ?, ?, ?)", 
                 (datetime.datetime.now().isoformat(), "VAULT_SEAL", float(int(seal[:10], 16)), "SYSTEM_CORE"))
    conn.commit()
    conn.close()
    print(f"🔒 [OMEGA] Vault sellado criptográficamente: {seal[:16]}...")

if __name__ == "__main__":
    integrity_seal()
