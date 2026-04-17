import sqlite3, json

def audit():
    db = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db)
    results = {}
    
    # Ámbito 1: Integridad de datos
    results["1_Integridad"] = conn.execute("SELECT count(*) FROM cases").fetchone()[0]
    # Ámbito 2: Riesgo promedio
    results["2_Riesgo_Promedio"] = conn.execute("SELECT avg(risk_score) FROM cases").fetchone()[0]
    # Ámbito 3: Entidades extraídas
    results["3_Entidades_Forenses"] = conn.execute("SELECT count(*) FROM entities").fetchone()[0]
    # Ámbito 4: Casos vinculados
    results["4_Casos_Vinculados"] = conn.execute("SELECT count(*) FROM relations").fetchone()[0]
    # Ámbito 5: Fuente dominante
    results["5_Medio_Principal"] = conn.execute("SELECT fuente, count(*) as c FROM cases GROUP BY fuente ORDER BY c DESC LIMIT 1").fetchone()
    # Ámbito 6: Picos de violencia (Días de fuego)
    results["6_Picos_Violencia"] = conn.execute("SELECT fecha_pub, count(*) as c FROM cases GROUP BY fecha_pub ORDER BY c DESC LIMIT 1").fetchone()
    # Ámbito 7: Análisis de modalidades (Sicariato)
    results["7_Sicariato_Count"] = conn.execute("SELECT count(*) FROM cases WHERE titular LIKE \"%sicariato%\"").fetchone()[0]
    # Ámbito 8: Inteligencia de víctimas
    results["8_Victimas_Identificadas"] = conn.execute("SELECT count(*) FROM entities WHERE tipo=\"VICTIMA\"").fetchone()[0]
    # Ámbito 9: Presencia Geográfica
    results["9_Cantones_Cubiertos"] = conn.execute("SELECT count(DISTINCT canton) FROM cases WHERE canton IS NOT NULL").fetchone()[0]
    # Ámbito 10: Estado de Integridad criptográfica
    results["10_Vault_Seal"] = conn.execute("SELECT valor FROM external_factors WHERE variable=\"VAULT_SEAL\" ORDER BY id DESC LIMIT 1").fetchone()[0]
    
    with open("/home/ubuntu/elysium_audit_report.json", "w") as f:
        json.dump(results, f, indent=4)
    print("✅ Auditoría en 10 ámbitos completada. Reporte en ~/elysium_audit_report.json")

if __name__ == "__main__":
    audit()
