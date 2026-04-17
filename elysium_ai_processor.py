import sqlite3, json, requests

class ElysiumForensicAI:
    def __init__(self, model="llama3.2:1b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"
        self.db_path = "/home/ubuntu/elysium_intel_v2.db"

    def audit_text(self, text):
        prompt = f"""
        ACTÚA COMO AUDITOR FORENSE.
        Analiza el texto y extrae UNICAMENTE un JSON con:
        - nombres_victimas: [lista]
        - alias_mencionados: [lista]
        - bandas_criminales: [lista]
        - arma_especifica: string
        - es_ajuste_cuentas: boolean
        Texto: {text[:2000]}
        """
        try:
            r = requests.post(self.api_url, json={"model": self.model, "prompt": prompt, "stream": False, "format": "json"}, timeout=60)
            return json.loads(r.json().get("response", "{}"))
        except: return None

    def execute_intelligence_cycle(self):
        print("🧠 [AI-FORENSIC] Iniciando Ciclo de Inteligencia Profunda...")
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT id_caso, contenido_completo FROM cases WHERE contenido_completo IS NOT NULL LIMIT 5").fetchall()
            
            for row in rows:
                print(f"   ► Procesando evidencias de: {row[id_caso]}...")
                intel = self.audit_text(row["contenido_completo"])
                if intel:
                    # Inyectar en tabla de entidades para el Knowledge Graph
                    for v in intel.get("nombres_victimas", []):
                        conn.execute("INSERT INTO entities (id_caso, tipo, valor) VALUES (?, ?, ?)", (row["id_caso"], "VICTIMA", v))
                    for b in intel.get("bandas_criminales", []):
                        conn.execute("INSERT INTO entities (id_caso, tipo, valor) VALUES (?, ?, ?)", (row["id_caso"], "BANDA", b))
                    print(f"      ✅ Inteligencia extraída y vinculada.")

if __name__ == "__main__":
    ai = ElysiumForensicAI()
    ai.execute_intelligence_cycle()
