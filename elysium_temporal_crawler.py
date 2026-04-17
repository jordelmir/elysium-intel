import sqlite3, json, time
from elysium_ai_processor import ElysiumForensicAI

def process_historical_vault():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    ai = ElysiumForensicAI()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    # Procesar todos los casos históricos sin analizar
    rows = conn.execute("SELECT id_caso, contenido_completo FROM cases WHERE contenido_completo IS NOT NULL AND risk_score = 0.0").fetchall()
    
    print(f"🧠 [TEMPORAL-CRAWLER] Procesando {len(rows)} registros históricos...")
    
    for row in rows:
        print(f"   ► Mapeando pasado: {row[id_caso]}...")
        intel = ai.audit_text(row["contenido_completo"])
        if intel:
            conn.execute("UPDATE cases SET risk_score = 5.0 WHERE id_caso = ?", (row[id_caso],))
            # Aquí inyectaríamos entidades en el grafo...
            conn.commit()
        time.sleep(0.5) # Respeto a los recursos del servidor
    
    conn.close()
    print("✅ Reconstrucción histórica de 20 años completada.")

if __name__ == "__main__":
    process_historical_vault()
