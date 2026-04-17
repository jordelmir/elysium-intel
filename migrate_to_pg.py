import sqlite3, psycopg2

def get_pass():
    with open("/home/ubuntu/.elysium_pg_pass", "r") as f:
        return f.read().strip()

def migrate():
    print("🔄 [MIGRATION] Iniciando migración masiva a PostgreSQL...")
    src = sqlite3.connect("/home/ubuntu/elysium_intel_v2.db")
    dst = psycopg2.connect(host="localhost", dbname="elysium_intel", user="elysium_api", password=get_pass())
    
    # Asegurar esquema
    dst.cursor().execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id_caso TEXT PRIMARY KEY,
            fecha_pub TEXT,
            fuente TEXT,
            titular TEXT,
            url TEXT,
            contenido_completo TEXT,
            risk_score REAL
        )
    """)
    dst.commit()
    
    src_cur = src.cursor()
    rows = src_cur.execute("SELECT id_caso, fecha_pub, fuente, titular, url, contenido_completo, risk_score FROM cases").fetchall()
    
    batch = []
    for row in rows:
        batch.append(row)
        if len(batch) >= 500:
            dst.cursor().executemany("INSERT INTO cases VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", batch)
            dst.commit()
            batch = []
            
    if batch:
        dst.cursor().executemany("INSERT INTO cases VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", batch)
        dst.commit()
        
    print(f"✅ Migración finalizada: {len(rows)} registros movidos a TimescaleDB.")

if __name__ == "__main__":
    migrate()
