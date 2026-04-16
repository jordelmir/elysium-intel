from playwright.async_api import async_playwright
import asyncio, json

TARGETS_INTERCEPT = {
    "La Nación": {
        "goto": "https://www.nacion.com/sucesos/",
        "intercept_domains": ["api.nacion.com", "arc-pub", "cdn.nacion"],
        "json_path": ["content_elements", "items", "stories"],
    },
    "Teletica": {
        "goto": "https://www.teletica.com/sucesos",
        "intercept_domains": ["api.teletica.com", "teletica.com/api"],
        "json_path": ["data", "items", "articles"],
    },
}

async def intercept_source(name, config, keywords):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(user_agent="Mozilla/5.0")
        page = await context.new_page()

        async def on_response(response):
            if any(d in response.url for d in config["intercept_domains"]):
                try:
                    data = await response.json()
                    for kw in keywords:
                        if kw.lower() in str(data).lower():
                            results.append({
                                "fuente": name, 
                                "titular": "HALLAZGO XHR INTERCEPT", 
                                "url": response.url, 
                                "capa": "PLAYWRIGHT"
                            })
                            break
                except: pass

        page.on("response", on_response)
        try:
            await page.goto(config["goto"], wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(5)
        except Exception: pass
        finally: await browser.close()
    return results
