import sqlite3, json

def analyze_victims():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    stats = {"sexo": {"M": 0, "F": 0, "Desconocido": 0}, "edad": {"Niño": 0, "Joven": 0, "Adulto": 0, "Adulto Mayor": 0}}
    
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT titular FROM cases WHERE id_caso LIKE \"CR-2025-%\"").fetchall()
        
        for row in rows:
            t = row["titular"].lower()
            # Análisis de Sexo
            if "hombre" in t or "varón" in t or "masculino" in t: stats["sexo"]["M"] += 1
            elif "mujer" in t or "femenina" in t or "femenino" in t: stats["sexo"]["F"] += 1
            else: stats["sexo"]["Desconocido"] += 1
            
            # Análisis de Edad (Estimación Semántica)
            if "niño" in t or "menor" in t or "bebé" in t: stats["edad"]["Niño"] += 1
            elif "joven" in t or "muchacho" in t or "estudiante" in t: stats["edad"]["Joven"] += 1
            elif "anciano" in t or "adulto mayor" in t or "abuelo" in t: stats["edad"]["Adulto Mayor"] += 1
            else: stats["edad"]["Adulto"] += 1
            
    return stats

if __name__ == "__main__":
    results = analyze_victims()
    print("\n--- ⚖️ PERFIL DE VÍCTIMAS 2025 (ANÁLISIS DE INTELIGENCIA) ---")
    print(json.dumps(results, indent=2, ensure_ascii=False))
