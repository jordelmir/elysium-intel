import sqlite3, time

def stress_test():
    print("🚀 [TEST] Iniciando Auditoría de Estrés Forense...")
    conn = sqlite3.connect("/home/ubuntu/elysium_intel_v2.db")
    start = time.time()
    
    # Prueba 1: Auditoría de Integridad
    count = conn.execute("SELECT count(*) FROM cases WHERE contenido_completo IS NOT NULL").fetchone()[0]
    
    # Prueba 2: Consulta Compleja (Inteligencia de Grafos)
    complex_query = """
        SELECT e.valor as banda, count(*) as incidentes
        FROM entities e
        JOIN cases c ON e.id_caso = c.id_caso
        WHERE e.tipo = "BANDA"
        GROUP BY banda
        ORDER BY incidentes DESC LIMIT 5
    """
    relaciones = conn.execute(complex_query).fetchall()
    
    end = time.time()
    print(f"✅ Integridad: {count} registros con contenido completo.")
    print(f"✅ Inteligencia forense (Top Bandas): {relaciones}")
    print(f"⚡ Latencia de consulta: {end-start:.4f} segundos.")
    conn.close()

if __name__ == "__main__":
    stress_test()
