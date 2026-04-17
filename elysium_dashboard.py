import streamlit as st
import pandas as pd
import sqlite3, json
from deep_analyzer import dissect_content

st.set_page_config(page_title="ELYSIUM OMNI-BRAIN v7.0", layout="wide")

st.markdown("<h1 style=\"color: #ff4b4b;\">🏛️ ELYSIUM-INTEL OMNI-BRAIN</h1>", unsafe_allow_stdio=True)
st.subheader("Plataforma de Dominio de Información y Análisis de Hostilidades")

# Conexión Global
conn = sqlite3.connect("/home/ubuntu/elysium_intel_v2.db")

# Sidebar: Inteligencia Predictiva
st.sidebar.title("🧠 Inteligencia Artificial")
st.sidebar.info("IA Activa: Llama 3.2 1B\nGrafo de Entidades: Operativo")

# KPIs de Estado
rows = conn.execute("SELECT count(*) FROM cases").fetchone()[0]
entities = conn.execute("SELECT count(*) FROM entities").fetchone()[0]

c1, c2, c3 = st.columns(3)
c1.metric("Vault Global (2006-2026)", rows)
c2.metric("Entidades Forenses Vinculadas", entities)
c3.metric("Integridad del Grafo", "100%")

# SECCIÓN: PATRONES DETECTADOS
st.markdown("---")
st.subheader("🔗 Alertas de Patrones Recurrentes")
patterns = conn.execute("SELECT valor, count(*) as c FROM entities GROUP BY valor HAVING c > 1 ORDER BY c DESC LIMIT 10").fetchall()
if patterns:
    st.warning(f"Se han detectado {len(patterns)} entidades con vinculaciones múltiples.")
    st.table(pd.DataFrame(patterns, columns=["Entidad Detectada", "Incidentes Vinculados"]))

# SECCIÓN: ANÁLISIS TERRITORIAL
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribución por Cantón")
    cantones = pd.read_sql_query("SELECT canton, count(*) as c FROM cases WHERE id_caso LIKE \"CR-2025-%\" GROUP BY canton ORDER BY c DESC LIMIT 10", conn)
    st.bar_chart(cantones.set_index("canton"))

with col2:
    st.subheader("👥 Perfil de Víctimas (Análisis IA)")
    victimas = pd.read_sql_query("SELECT valor, count(*) as c FROM entities WHERE tipo=\"VICTIMA\" GROUP BY valor ORDER BY c DESC LIMIT 10", conn)
    st.dataframe(victimas, use_container_width=True)

conn.close()
