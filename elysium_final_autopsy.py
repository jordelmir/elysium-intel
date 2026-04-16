import sqlite3, json, sys
from deep_analyzer import dissect_content

class ElysiumFinalAutopsy:
    def __init__(self):
        self.db_path = "/home/ubuntu/elysium_intel_v2.db"

    def execute_autopsy(self):
        print("🏛️ [AUTOPSIA-FINAL] Iniciando disección del 100% de los casos (2025)...")
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT id_caso, titular FROM cases WHERE id_caso LIKE \"CR-2025-%\" LIMIT 500").fetchall()
            
            stats = {"provincias": {}, "cantones": {}, "distritos": {}, "motivos": {}}
            
            for row in rows:
                intel = dissect_content(row["titular"])
                
                # Agregación de Inteligencia
                stats["provincias"][intel["provincia"]] = stats["provincias"].get(intel["provincia"], 0) + 1
                stats["cantones"][intel["canton"]] = stats["cantones"].get(intel["canton"], 0) + 1
                stats["distritos"][intel["distrito"]] = stats["distritos"].get(intel["distrito"], 0) + 1
                stats["motivos"][intel["motivo"]] = stats["motivos"].get(intel["motivo"], 0) + 1
            
            return stats

if __name__ == "__main__":
    autopsy = ElysiumFinalAutopsy()
    stats = autopsy.execute_autopsy()
    
    print("\n--- ⚖️ ANÁLISIS FORENSE AGREGADO (DISTRITOS Y MOTIVOS) ---")
    print(f"📊 TOP MOTIVOS: {json.dumps(stats["motivos"], indent=2, ensure_ascii=False)}")
    print(f"📊 TOP DISTRITOS: {json.dumps(dict(sorted(stats["distritos"].items(), key=lambda x: x[1], reverse=True)[:5]), indent=2, ensure_ascii=False)}")
    print(f"📊 TOP CANTONES: {json.dumps(dict(sorted(stats["cantones"].items(), key=lambda x: x[1], reverse=True)[:5]), indent=2, ensure_ascii=False)}")
