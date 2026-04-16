import asyncio, os, time
from elysium_homicidio_core import run_full_scan
from elysium_sentinel import ElysiumSentinel

async def main():
    print("🧠 [ORQUESTADOR] Iniciando ciclo de inteligencia 24/7...")
    start_time = time.time()
    
    # 1. Escaneo Triple Capa (RSS + GNews + XHR)
    print("📡 Fase 1: Recolección Multicapa...")
    casos = await run_full_scan()
    
    # 2. Análisis y Filtrado de Sentinel (Alertas Críticas)
    print("🚨 Fase 2: Alertas Críticas Sentinel...")
    sentinel = ElysiumSentinel()
    for caso in casos[:3]: # Alerta solo de los 3 casos más recientes detectados
        sentinel.send_alert(caso)
        
    # 3. Respaldo del Vault
    print("📦 Fase 3: Respaldo del Vault...")
    os.system("bash ~/elysium_homicidio/elysium_backup.sh")
    
    duration = time.time() - start_time
    print(f"✅ Ciclo Completado con éxito en {duration:.2f}s. Sistema en Standby.")

if __name__ == "__main__":
    asyncio.run(main())
