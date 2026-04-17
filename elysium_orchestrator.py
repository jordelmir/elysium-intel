import asyncio, os, time, sqlite3
from elysium_homicidio_core import run_full_scan
from elysium_deep_scout import infiltrate_content
from elysium_ai_processor import ElysiumForensicAI
from elysium_sentinel import ElysiumSentinel

async def execute_omni_cycle():
    print("🧠 [OMNI-BRAIN] Iniciando Ciclo de Inteligencia Total v7.0...")
    start_ts = time.time()
    sentinel = ElysiumSentinel()

    # 1. SCAN: Recolección Multicapa (Presente)
    print("📡 FASE 1: Recolección Multicapa...")
    nuevos_casos = await run_full_scan()

    # 2. SCOUT: Infiltración de Contenido Profundo
    print("🕵️ FASE 2: Infiltración de Evidencias Digitales...")
    await infiltrate_content()

    # 3. NEURAL: Auditoría Forense por IA
    print("🤖 FASE 3: Auditoría Neuronal y Extracción de Entidades...")
    ai = ElysiumForensicAI()
    ai.execute_intelligence_cycle()

    # 4. PATTERN: Descubrimiento de Vínculos (Knowledge Graph)
    print("🔗 FASE 4: Análisis de Patrones y Vínculos...")
    with sqlite3.connect("/home/ubuntu/elysium_intel_v2.db") as conn:
        # Detectar nombres recurrentes (Potenciales objetivos o victimarios)
        duplicates = conn.execute("""
            SELECT valor, count(*) as menciones 
            FROM entities 
            WHERE tipo="VICTIMA" 
            GROUP BY valor HAVING menciones > 1
        """).fetchall()
        for d in duplicates:
            print(f"   ⚠️ PATRÓN DETECTADO: {d[0]} mencionado en {d[1]} casos.")

    # 5. BACKUP & CLEANUP
    os.system("bash ~/elysium_homicidio/elysium_backup.sh")
    
    print(f"✅ CICLO OMNI COMPLETADO: {time.time() - start_ts:.2f}s. Intelligence Vault Actualizado.")

if __name__ == "__main__":
    os.system("bash ~/elysium_homicidio/sync_to_web.sh")
    asyncio.run(execute_omni_cycle())
