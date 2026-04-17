import sqlite3

# Diccionario de alta precisión para geocoding local
LUGARES_PRECISOS = {
    "Cieneguita": (9.986, -83.027),
    "Pavas": (9.954, -84.132),
    "Hatillo": (9.914, -84.095),
    "Alajuelita": (9.893, -84.103)
}

def get_coords(text):
    for lugar, coords in LUGARES_PRECISOS.items():
        if lugar.lower() in text.lower():
            return coords
    return None

def run_geo_parser():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    # Crear columnas si no existen
    try:
        conn.execute("ALTER TABLE cases ADD COLUMN lat REAL")
        conn.execute("ALTER TABLE cases ADD COLUMN lon REAL")
    except: pass
    
    rows = conn.execute("SELECT id_caso, titular FROM cases WHERE lat IS NULL").fetchall()
    for row in rows:
        coords = get_coords(row[1])
        if coords:
            conn.execute("UPDATE cases SET lat = ?, lon = ? WHERE id_caso = ?", (coords[0], coords[1], row[0]))
    conn.commit()
    conn.close()
    print("✅ [GEO-PARSER] Mapeo de precisión alta completado.")

if __name__ == "__main__":
    run_geo_parser()
