import feedparser, urllib.parse

GOOGLE_NEWS_QUERIES = [
    "homicidio Costa Rica", "asesinato Costa Rica", "balacera Costa Rica", "sicariato Costa Rica"
]

def scan_google_news(query):
    q = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={q}&hl=es-419&gl=CR&ceid=CR:es-419"
    feed = feedparser.parse(url)
    return [{
        "fuente": entry.get("source",{}).get("title","GNews"),
        "titular": entry.get("title",""),
        "url": entry.get("link",""),
        "capa": "GNEWS",
        "confiabilidad": "MEDIA",
        "fecha_pub": entry.get("published", "")
    } for entry in feed.entries]
