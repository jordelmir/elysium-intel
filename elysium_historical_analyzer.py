import sqlite3, json
from datetime import datetime

RISK_WEIGHTS = {"sicariato": 9.5, "balacera": 8.5, "hallazgo": 7.0, "riña": 5.0}

def calculate_risk(titular):
    score = 3.0
    for key, weight in RISK_WEIGHTS.items():
        if key in titular.lower():
            score = max(score, weight)
    return score

def run_historical_analysis():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Análisis forense total desde 2006 hasta 2026
    print("🧠 [HISTORICAL-ANALYZER] Iniciando autopsia forense de 20 años...")
    
    rows = cur.execute("SELECT id_caso, titular, fecha_pub FROM cases").fetchall()
    
    for row in rows:
        id_caso, titular, fecha = row
        score = calculate_risk(titular)
        cur.execute("UPDATE cases SET risk_score = ? WHERE id_caso = ?", (score, id_caso))
    
    conn.commit()
    
    # Generar reporte de picos históricos
    top_picos = cur.execute("""
        SELECT substr(fecha_pub, 1, 4) as anio, count(*) as total, avg(risk_score) as avg_risk 
        FROM cases 
        GROUP BY anio 
        ORDER BY total DESC
    """).fetchall()
    
    print("\n--- ⚖️ ELYSIUM: ANÁLISIS FORENSE HISTÓRICO (2006-2026) ---")
    for anio, total, avg_r in top_picos:
        print(f"Año: {anio} | Homicidios: {total} | Riesgo Promedio: {avg_r:.2f}")

    conn.close()

if __name__ == "__main__":
    run_historical_analysis()
