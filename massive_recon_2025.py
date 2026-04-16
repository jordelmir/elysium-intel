import feedparser, urllib.parse, time, sqlite3, hashlib
from datetime import datetime, timedelta

class MassiveRecon:
    def __init__(self):
        self.db_path = "/home/ubuntu/elysium_intel_v2.db"
        self.kws = ["homicidio", "asesinato", "sicariato", "balacera"]
        self._setup_db()

    def _setup_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS cases (id_caso TEXT PRIMARY KEY, fuente TEXT, url TEXT, titular TEXT, fecha_pub TEXT, capa TEXT)")

    def get_weeks(self, year):
        start_date = datetime(year, 1, 1)
        weeks = []
        for i in range(52):
            end_date = start_date + timedelta(days=7)
            weeks.append((start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
            start_date = end_date
        return weeks

    def run(self):
        weeks = self.get_weeks(2025)
        total_found = 0
        
        for start, end in weeks:
            print(f"🕵️ [RECON] Escaneando semana: {start} al {end}...")
            for kw in self.kws:
                query = f"{kw} Costa Rica after:{start} before:{end}"
                q_enc = urllib.parse.quote(query)
                url = f"https://news.google.com/rss/search?q={q_enc}&hl=es-419&gl=CR&ceid=CR:es-419"
                
                feed = feedparser.parse(url)
                batch = []
                for entry in feed.entries:
                    titular = entry.get("title", "")
                    link = entry.get("link", "")
                    # Generar ID único basado en el link para evitar duplicados en DB
                    id_hash = hashlib.md5(link.encode()).hexdigest()[:12]
                    id_caso = f"CR-2025-{id_hash}"
                    
                    batch.append((id_caso, entry.get("source", {}).get("title", "GNews"), link, titular, entry.get("published", ""), "MASSIVE-RECON"))
                
                if batch:
                    with sqlite3.connect(self.db_path) as conn:
                        conn.executemany("INSERT OR IGNORE INTO cases (id_caso, fuente, url, titular, fecha_pub, capa) VALUES (?, ?, ?, ?, ?, ?)", batch)
                    total_found += len(batch)
                
                time.sleep(0.5) # Evitar baneo de Google
            
            # Mostrar progreso cada 4 semanas
            if weeks.index((start, end)) % 4 == 0:
                print(f"   📈 Progreso: {total_found} registros acumulados...")

        print(f"\n🏆 EXTRACCIÓN MASIVA COMPLETADA: {total_found} registros brutos procesados.")

if __name__ == "__main__":
    MassiveRecon().run()
