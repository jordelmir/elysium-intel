import sqlite3, pandas as pd
from datetime import datetime, timedelta

def get_prediction():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    # Cargar datos temporales
    df = pd.read_sql_query("SELECT fecha_pub, count(*) as count FROM cases GROUP BY fecha_pub", conn)
    conn.close()
    
    # Análisis de tendencia simple (promedio móvil)
    df["fecha_pub"] = pd.to_datetime(df["fecha_pub"], errors="coerce")
    df = df.dropna().set_index("fecha_pub").resample("W").sum()
    
    # Predecir próxima semana basándose en la tendencia de las últimas 4
    trend = df["count"].rolling(window=4).mean().iloc[-1]
    return trend

if __name__ == "__main__":
    trend = get_prediction()
    print(f"\n🚀 [ELYSIUM-FORECASTER] Predicción de riesgo para la próxima semana: {trend:.1f} incidentes estimados.")
