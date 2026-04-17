import sqlite3

def build_graph():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    # Vincular casos que comparten el mismo alias/nombre
    conn.execute("""
        CREATE TABLE IF NOT EXISTS relations (
            id INTEGER PRIMARY KEY,
            caso_a TEXT,
            caso_b TEXT,
            vinculo TEXT
        )
    """)
    # Buscar entidades repetidas
    matches = conn.execute("""
        SELECT e1.id_caso, e2.id_caso, e1.valor
        FROM entities e1
        JOIN entities e2 ON e1.valor = e2.valor
        WHERE e1.id_caso < e2.id_caso AND e1.tipo = "VICTIMA"
    """).fetchall()
    
    for c1, c2, val in matches:
        conn.execute("INSERT OR IGNORE INTO relations (caso_a, caso_b, vinculo) VALUES (?, ?, ?)", (c1, c2, f"Comparten victima/actor: {val}"))
    conn.commit()
    conn.close()
    print(f"🔗 [GRAPH-ENGINE] Se han creado {len(matches)} nuevos vínculos forenses.")

if __name__ == "__main__":
    build_graph()
