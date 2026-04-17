import asyncio, sqlite3
from playwright.async_api import async_playwright

async def infiltrate_content():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        c = await b.new_context(user_agent="Mozilla/5.0")
        
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            # Buscar casos sin contenido extraído
            rows = conn.execute("SELECT id_caso, url FROM cases WHERE contenido_completo IS NULL AND url LIKE \"http%\" LIMIT 10").fetchall()
            
            for row in rows:
                print(f"🕵️ [DEEP-SCOUT] Infiltrando: {row["id_caso"]}...")
                page = await c.new_page()
                try:
                    await page.goto(row["url"], timeout=30000, wait_until="domcontentloaded")
                    # Extraer texto de párrafos (limpieza básica de ruido)
                    text = await page.evaluate("() => Array.from(document.querySelectorAll(\"p\")).map(p => p.innerText).join(\"\\n\")")
                    if len(text) > 100:
                        conn.execute("UPDATE cases SET contenido_completo = ? WHERE id_caso = ?", (text, row["id_caso"]))
                        print(f"   ✅ Contenido asegurado ({len(text)} chars)")
                except:
                    print(f"   ❌ Fallo en infiltración")
                await page.close()
        await b.close()

if __name__ == "__main__":
    asyncio.run(infiltrate_content())
