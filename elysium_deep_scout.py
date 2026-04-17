import asyncio, sqlite3
from playwright.async_api import async_playwright

async def infiltrate_cache():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        c = await b.new_context(user_agent="Mozilla/5.0")
        page = await c.new_page()
        with sqlite3.connect(db_path) as conn:
            rows = conn.execute("SELECT id_caso, url FROM cases WHERE contenido_completo IS NULL LIMIT 5").fetchall()
            for row in rows:
                id_caso, url = row
                print(f"🕵️ [CACHE-SCOUT] Infiltrando: {id_caso}...")
                cache_url = f"https://webcache.googleusercontent.com/search?q=cache:{url}"
                try:
                    await page.goto(cache_url, timeout=20000)
                    text = await page.evaluate("() => document.body.innerText")
                    conn.execute("UPDATE cases SET contenido_completo = ? WHERE id_caso = ?", (text, id_caso))
                    conn.commit()
                    print(f"   ✅ Contenido asegurado")
                except: print("   ❌ Fallo en caché")
        await b.close()

if __name__ == "__main__":
    asyncio.run(infiltrate_cache())
