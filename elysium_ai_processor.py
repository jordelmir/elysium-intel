import sqlite3, json, requests

class ElysiumForensicAI:
    def __init__(self, model="llama3.2:1b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"
        self.db_path = "/home/ubuntu/elysium_intel_v2.db"

    def audit_text(self, text):
        # Prompt optimizado para modelos ligeros (1B)
        prompt = f"Extrae: victimas, arma, motivo. JSON solo: {text[:500]}"
        try:
            r = requests.post(self.api_url, json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }, timeout=60)
            return json.loads(r.json().get("response", "{}"))
        except: return None

    def execute_intelligence_cycle(self):
        print("🧠 [AI-FORENSIC-LOCAL] Iniciando ciclo gratuito...")
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT id_caso, contenido_completo FROM cases WHERE contenido_completo IS NOT NULL AND id_caso LIKE \"CR-2025-%\" LIMIT 5").fetchall()
            for row in rows:
                intel = self.audit_text(row["contenido_completo"])
                if intel:
                    print(f"   ✅ Inteligencia: {intel}")

if __name__ == "__main__":
    ai = ElysiumForensicAI()
    ai.execute_intelligence_cycle()
