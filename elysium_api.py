from fastapi import FastAPI
import sqlite3, json

app = FastAPI(title="ELYSIUM INTEL API v1.0", description="Servicio de Inteligencia de Seguridad Pública CR")
DB_PATH = "/home/ubuntu/elysium_intel_v2.db"

@app.get("/casos/total")
def get_total():
    with sqlite3.connect(DB_PATH) as conn:
        res = conn.execute("SELECT count(*) FROM cases").fetchone()
        return {"total_casos_registrados": res[0]}

@app.get("/casos/2025")
def get_2025():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute("SELECT * FROM cases WHERE id_caso LIKE \"CR-2025-%\" LIMIT 100").fetchall()
        return [dict(row) for row in res]

@app.get("/analisis/provincias")
def get_provincias():
    # Esta lógica se puede expandir para usar geo_intel.py
    return {"status": "success", "data": "Endpoint de análisis geográfico activo"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
