import asyncio, json, os, sqlite3
from datetime import datetime
from rss_layer            import scan_rss, RSS_SOURCES
from google_news_layer    import scan_google_news, GOOGLE_NEWS_QUERIES
from dedup                import deduplicar
from geo_intel            import analizar_caso

KEYWORDS_PRIMARY = ["homicidio","asesinato","balacera","sicariato","crimen","muerto"]

async def run_full_scan():
    all_raw = []
    print("\n╔═══ [CAPA 1-2] EXTRACCIÓN Y GEO-INTEL ═══╗")
    
    # Capa 1: RSS
    for name, url in RSS_SOURCES.items():
        try:
            hits = scan_rss(name, url, KEYWORDS_PRIMARY)
            all_raw.extend(hits)
        except Exception: pass

    # Capa 2: GNews
    for q in GOOGLE_NEWS_QUERIES[:2]:
        hits = scan_google_news(q)
        all_raw.extend(hits)

    # ── ANÁLISIS GEO ──
    unique = deduplicar(all_raw)
    for c in unique:
        intel = analizar_caso(c["titular"])
        c.update(intel)

    # ── GENERACIÓN DE REPORTE ──
    stats_prov = {}
    for c in unique:
        stats_prov[c["provincia"]] = stats_prov.get(c["provincia"], 0) + 1
    
    print(f"  🎯 Casos únicos procesados: {len(unique)}")
    print(f"  📊 Distribución por Provincia:\n{json.dumps(stats_prov, indent=4, ensure_ascii=False)}")
    
    # Vault persistence
    vault_dir = "/home/ubuntu/elysium_vault"
    os.makedirs(vault_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H%M")
    with open(f"{vault_dir}/scan_{ts}.json", "w") as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)
    print(f"  💾 Vault actualizado: scan_{ts}.json")
    return unique

if __name__ == "__main__":
    asyncio.run(run_full_scan())
