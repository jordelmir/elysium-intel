import sqlite3, json, pandas as pd

def find_fire_days():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT fecha_pub, count(*) as count FROM cases WHERE id_caso LIKE \"CR-2025-%\" GROUP BY fecha_pub", conn)
    conn.close()
    
    # Filtrar días con más de 5 homicidios (Olas de Violencia)
    fire_days = df[df["count"] > 5].sort_values(by="count", ascending=False)
    return fire_days.to_dict(orient="records")

if __name__ == "__main__":
    results = find_fire_days()
    print("\n--- 🔥 ELYSIUM ANALYTICS: CLUSTERS DE VIOLENCIA 2025 ---")
    print(json.dumps(results[:10], indent=2, ensure_ascii=False))
