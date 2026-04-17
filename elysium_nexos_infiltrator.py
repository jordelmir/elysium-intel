import sqlite3, urllib.parse, feedparser

def hunt_nexos():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    # Query de máxima penetración forense
    query = "(PLN OR \"Partido Liberación Nacional\") AND (OIJ OR \"Poder Judicial\" OR fiscalia) AND (corrupción OR narco OR narcotráfico OR sicariato)"
    print(f"📡 [NEXUS-HUNT] Iniciando infiltración de nexos políticos-judiciales...")
    
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=es-419&gl=CR&ceid=CR:es-419"
    feed = feedparser.parse(url)
    
    found = []
    for entry in feed.entries:
        found.append(("2026-NEXUS", "NEXO", entry.get("title", ""), entry.get("link", ""), "Nexos Poder", "Cross-Source"))
    
    with sqlite3.connect(db_path) as conn:
        conn.executemany("INSERT INTO cases (id_caso, fecha_pub, fuente, titular, url) VALUES (?, ?, ?, ?, ?)", found)
    print(f"✅ {len(found)} hallazgos sobre nexos de poder asegurados en el Vault.")

if __name__ == "__main__":
    hunt_nexos()
