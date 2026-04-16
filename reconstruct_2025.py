import feedparser, urllib.parse, json
from dedup import deduplicar

def get_2025_data():
    query = "homicidio Costa Rica after:2025-01-01 before:2025-12-31"
    q_enc = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={q_enc}&hl=es-419&gl=CR&ceid=CR:es-419"
    
    print(f"📡 [RECON-2025] Extrayendo cronología criminal de Google News...")
    feed = feedparser.parse(url)
    raw_cases = []
    
    for entry in feed.entries:
        raw_cases.append({
            "fuente": entry.get("source", {}).get("title", "GNews"),
            "titular": entry.get("title", ""),
            "url": entry.get("link", ""),
            "fecha": entry.get("published", "")
        })
    
    unique_cases = deduplicar(raw_cases)
    
    # Análisis rápido
    stats = {"San José": 0, "Limón": 0, "Puntarenas": 0, "Alajuela": 0, "Otros": 0}
    for c in unique_cases:
        t = c["titular"].lower()
        if "limón" in t or "limon" in t: stats["Limón"] += 1
        elif "san josé" in t or "san jose" in t: stats["San José"] += 1
        elif "puntarenas" in t: stats["Puntarenas"] += 1
        elif "alajuela" in t: stats["Alajuela"] += 1
        else: stats["Otros"] += 1
            
    return unique_cases, stats

if __name__ == "__main__":
    cases, stats = get_2025_data()
    print(f"\n🏆 RECONSTRUCCIÓN 2025 COMPLETADA")
    print(f"🎯 Casos Únicos Identificados: {len(cases)}")
    print(f"📊 Distribución Geográfica (Mención en Titular): {json.dumps(stats, indent=2, ensure_ascii=False)}")
    print("\n--- ⚖️ MUESTRA DE CASOS 2025 ---")
    for c in cases[:10]:
        print(f"  • [{c["fuente"]}] {c["titular"][:80]}...")
