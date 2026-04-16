import feedparser, urllib.parse, time, sqlite3, hashlib, sys
from datetime import datetime, timedelta

class ElysiumMegaRecon:
    def __init__(self, start_year, end_year):
        self.db_path = "/home/ubuntu/elysium_intel_v2.db"
        self.start_year = start_year
        self.end_year = end_year
        self.kws = ["homicidio", "asesinato", "sicariato", "balacera"]

    def run(self):
        print(f"🏛️ [MEGA-RECON] Iniciando Arqueología de Datos: {self.start_year} -> {self.end_year}")
        
        for year in range(self.start_year, self.end_year - 1, -1):
            print(f"\n📅 PROCESANDO AÑO: {year}")
            start_date = datetime(year, 1, 1)
            
            # Barrido semanal (52 semanas por año)
            for w in range(52):
                end_date = start_date + timedelta(days=7)
                s_str = start_date.strftime("%Y-%m-%d")
                e_str = end_date.strftime("%Y-%m-%d")
                
                batch = []
                for kw in self.kws:
                    query = f"{kw} Costa Rica after:{s_str} before:{e_str}"
                    q_enc = urllib.parse.quote(query)
                    url = f"https://news.google.com/rss/search?q={q_enc}&hl=es-419&gl=CR&ceid=CR:es-419"
                    
                    feed = feedparser.parse(url)
                    for entry in feed.entries:
                        link = entry.get("link", "")
                        id_hash = hashlib.md5(link.encode()).hexdigest()[:12]
                        id_caso = f"CR-{year}-{id_hash}"
                        
                        batch.append((
                            id_caso, 
                            entry.get("source", {}).get("title", "GNews Archive"), 
                            link, 
                            entry.get("title", ""), 
                            entry.get("published", ""), 
                            "MEGA-RECON"
                        ))
                
                if batch:
                    with sqlite3.connect(self.db_path) as conn:
                        conn.executemany("INSERT OR IGNORE INTO cases (id_caso, fuente, url, titular, fecha_pub, capa) VALUES (?, ?, ?, ?, ?, ?)", batch)
                
                start_date = end_date
                # Log de progreso por semana
                sys.stdout.write(f"\r   📈 {year}: Semana {w+1}/52 completada...")
                sys.stdout.flush()
                time.sleep(0.3) # Sigilo profesional para evitar bloqueos
                
        print("\n\n🏆 OPERACIÓN DE ARQUEOLOGÍA COMPLETADA.")

if __name__ == "__main__":
    # Ejecutamos el primer gran bloque: 2026 down to 2006
    reconstructor = ElysiumMegaRecon(2026, 2006)
    reconstructor.run()
