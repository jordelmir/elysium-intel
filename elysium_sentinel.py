import os
from dotenv import load_dotenv
load_dotenv()
import requests

class ElysiumSentinel:
    def __init__(self, bot_token=None, chat_id=None):
        self.token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")

    def send_alert(self, caso):
        msg = f"🚨 *ALERTA DE INTELIGENCIA ELYSIUM*\n\n"
        msg += f"📌 *Evento:* {caso[titular]}\n"
        msg += f"📍 *Ubicación:* {caso.get(provincia, N/A)}, {caso.get(canton, N/A)}\n"
        msg += f"🔥 *Modalidad:* {caso.get(modalidad, N/A)}\n"
        msg += f"📰 *Fuente:* {caso[fuente]}\n\n"
        msg += f"🔗 [Ver Evidencia]({caso[url]})"
        
        # En una fase real, aquí haríamos el request a Telegram
        print(f"📡 [SENTINEL] Alerta preparada para: {caso[id_caso]}")
        return msg

if __name__ == "__main__":
    # Test de alerta
    test_case = {
        "id_caso": "CR-2026-TEST",
        "titular": "Balacera en Cieneguita deja un fallecido y dos heridos",
        "provincia": "Limón",
        "canton": "Limón",
        "modalidad": "sicariato",
        "fuente": "CRHoy",
        "url": "https://crhoy.com"
    }
    sentinel = ElysiumSentinel()
    print(sentinel.send_alert(test_case))
