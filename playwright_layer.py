import asyncio
from playwright.async_api import async_playwright

TARGETS = {
    "La Nación": {"goto": "https://www.nacion.com/sucesos/", "match": "api.nacion.com"},
    "Teletica": {"goto": "https://www.teletica.com/sucesos", "match": "api.teletica.com"}
}

async def intercept_xhr(name, config, keywords):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Reutilización de contexto para minimizar overhead de memoria
        context = await browser.new_context(user_agent="Mozilla/5.0")
        page = await context.new_page()

        async def handle_response(response):
            if config["match"] in response.url:
                try:
                    data = await response.json()
                    # Lógica de extracción de entidades pura desde JSON
                    if any(kw.lower() in str(data).lower() for kw in keywords):
                        results.append({"fuente": name, "titular": "XHR-INFILTRATION", "url": response.url})
                except: pass

        page.on("response", handle_response)
        try:
            await page.goto(config["goto"], wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(5)
        except: pass
        await browser.close()
    return results
