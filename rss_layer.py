import feedparser

RSS_SOURCES = {
    "La Nación":   "https://www.nacion.com/arc/outboundfeeds/rss/?outputType=xml",
    "CRHoy":       "https://crhoy.com/feed/",
    "Teletica":    "https://teletica.com/rss",
    "Delfino":     "https://delfino.cr/feed",
    "Ameliarueda": "https://ameliarueda.com/feed",
    "Diario Extra":"https://www.diarioextra.com/rss.xml",
}

def scan_rss(name, url, keywords):
    feed = feedparser.parse(url)
    hits = []
    for entry in feed.entries:
        text = (entry.get("title","") + " " + entry.get("summary","")).lower()
        if any(kw.lower() in text for kw in keywords):
            hits.append({
                "fuente": name,
                "titular": entry.get("title",""),
                "url": entry.get("link",""),
                "capa": "RSS",
                "confiabilidad": "ALTA",
                "fecha_pub": entry.get("published", "")
            })
    return hits
