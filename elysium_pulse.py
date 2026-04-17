import sqlite3
from deep_analyzer import dissect_content

def calculate_aggressiveness(titular):
    kws = ["acribillado", "masacre", "brutal", "decapitado", "tortura", "violento"]
    return sum(1 for kw in kws if kw in titular.lower())

def run_pulse():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT titular FROM cases WHERE fecha_pub LIKE \"2026-%\"").fetchall()
    
    total_score = sum(calculate_aggressiveness(r[0]) for r in rows)
    print(f"\n⚡ [ELYSIUM-PULSE] Índice de Temperatura Criminal CR (2026): {total_score}")
    
    if total_score > 50:
        print("⚠️ ALERTA: La semántica de la violencia está escalando a niveles críticos.")
    else:
        print("✅ NIVEL DE VIOLENCIA: Estable.")
    conn.close()

if __name__ == "__main__":
    run_pulse()
