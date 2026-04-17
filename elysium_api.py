from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3, json

app = FastAPI(title="ELYSIUM INTEL API v1.1")

# Configuración de Seguridad CORS para Vercel/Producción
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://elysium-intel.vercel.app"], # En producción real, pondríamos la URL de tu Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "/home/ubuntu/elysium_intel_v2.db"

@app.get("/")
def health():
    return {"status": "operational", "engine": "Omni-Brain v7.0"}

@app.get("/stats")
def get_stats():
    with sqlite3.connect(DB_PATH) as conn:
        total = conn.execute("SELECT count(*) FROM cases").fetchone()[0]
        entities = conn.execute("SELECT count(*) FROM entities").fetchone()[0]
        return {"total_cases": total, "total_entities": entities}

@app.get("/latest")
def get_latest():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute("SELECT id_caso, titular, fuente, url FROM cases ORDER BY id_caso DESC LIMIT 20").fetchall()
        return [dict(row) for row in res]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
