import hmac, hashlib, time, base64, asyncpg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
DB_CONFIG = "postgresql://elysium_api@localhost/elysium_intel"
SECRET = b"ELYSIUM_HARDWARE_KEY_2026"

class DumpRequest(BaseModel):
    device_id: str
    timestamp: int
    nonce: str
    payload: str
    hmac: str

@app.post("/api/ingest/dump")
async def ingest_dump(data: DumpRequest):
    # 1. Anti-Replay
    if abs(time.time() - data.timestamp) > 30:
        raise HTTPException(403, "expired")
        
    # 2. HMAC Validation
    msg = f"{data.device_id}{data.timestamp}{data.nonce}{data.payload}".encode()
    expected = hmac.new(SECRET, msg, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(data.hmac, expected):
        raise HTTPException(403, "auth_fail")

    # 3. DB Persistence
    payload_bytes = base64.b64decode(data.payload)
    sha256 = hashlib.sha256(payload_bytes).digest()
    
    conn = await asyncpg.connect(DB_CONFIG)
    await conn.execute("""
        INSERT INTO hardware_raw (sha256, source_device, raw_dump, hmac_signature, nonce) 
        VALUES ($1, $2, $3, decode($4, 'hex'), decode($5, 'hex'))
    """, sha256, data.device_id, payload_bytes, data.hmac, data.nonce)
    await conn.close()
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
