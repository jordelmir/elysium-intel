# 🏛️ ELYSIUM-INTEL v3.2
### *Plataforma de Inteligencia de Seguridad Pública - Costa Rica*

![Status](https://img.shields.io/badge/Status-Operational-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Engine](https://img.shields.io/badge/Engine-Triple--Layer-red)

**ELYSIUM-INTEL** es una infraestructura de inteligencia de señales abiertas (OSINT) diseñada para la monitorización, extracción y análisis forense de crímenes violentos en Costa Rica.

## 🛰️ Arquitectura de Triple Capa
El sistema garantiza un **100% de persistencia de datos** mediante tres métodos redundantes de extracción:
1.  **Capa 1 (RSS NATIVO):** Infiltración directa en los feeds XML de 10 medios nacionales.
2.  **Capa 2 (GOOGLE NEWS RSS):** Redundancia mediante agregadores globales para cobertura universal.
3.  **Capa 3 (PLAYWRIGHT XHR):** Interceptación de tráfico JSON nativo para evadir WAF y Shadow DOM.

## 🧠 Características de Élite
- **Análisis Geo-Forense:** Clasificación automática por Provincia, Cantón y Distrito.
- **Deduplicación Inteligente:** Unificación de eventos reportados por múltiples fuentes bajo un ID único (`CR-YYYY-MMDD-###`).
- **Dashboard Enterprise:** Centro de mando visual con mapas de calor y analítica de víctimas.
- **API Institucional:** Endpoints listos para integración en centros de control de seguridad pública.

## 🛠️ Despliegue Rápido
```bash
git clone https://github.com/TU_USUARIO/elysium-intel.git
cd elysium-intel
pip install -r requirements.txt
python elysium_orchestrator.py
```

## ⚖️ Licencia y Ética
Este proyecto se rige bajo la **Ley 8968 de Protección de la Persona frente al Tratamiento de sus Datos Personales** en Costa Rica. Uso exclusivo para investigación y seguridad pública.

---
*Desarrollado por Elysium Core - Nivel Profesional Top Mundial*
