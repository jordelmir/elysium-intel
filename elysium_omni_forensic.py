import sqlite3, json

RISK_WEIGHTS = {"sicariato": 9.5, "balacera": 8.5, "hallazgo": 7.0, "riña": 5.0}

def calculate_risk(titular):
    score = 3.0 # Base
    for key, weight in RISK_WEIGHTS.items():
        if key in titular.lower():
            score = max(score, weight)
    return score

def run_forensic_audit():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    # Crear tabla de auditoría forense si no existe
    conn.execute("ALTER TABLE cases ADD COLUMN risk_score REAL DEFAULT 0.0")
    
    rows = conn.execute("SELECT id_caso, titular FROM cases WHERE risk_score = 0.0").fetchall()
    print(f"⚖️ [FORENSIC-AUDIT] Auditoría de {len(rows)} casos pendientes...")
    
    for r in rows:
        score = calculate_risk(r[1])
        conn.execute("UPDATE cases SET risk_score = ? WHERE id_caso = ?", (score, r[0]))
    
    conn.commit()
    conn.close()
    print("✅ Auditoría Forense Finalizada.")

if __name__ == "__main__":
    run_forensic_audit()
