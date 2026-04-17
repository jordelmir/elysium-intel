import sqlite3, json

def discover_gang_wars():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    with sqlite3.connect(db_path) as conn:
        # Relacionar Bandas con Cantones para detectar conflictos territoriales
        query = """
            SELECT e.valor as banda, c.canton, count(*) as incidentes
            FROM entities e
            JOIN cases c ON e.id_caso = c.id_caso
            WHERE e.tipo = "BANDA" AND c.canton != "No detectado"
            GROUP BY e.valor, c.canton
            ORDER BY incidentes DESC
        """
        results = conn.execute(query).fetchall()
        return results

if __name__ == "__main__":
    conflicts = discover_gang_wars()
    print("\n--- ⚖️ ELYSIUM INTELLIGENCE: ANALISIS DE CONFLICTOS ---")
    for b, c, i in conflicts:
        print(f"🔥 Banda: {b} | Territorio: {c} | Hostilidades: {i}")
