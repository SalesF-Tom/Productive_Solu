import os
import requests
import logging

def enviar_a_discord(mensaje: str):
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    if not webhook_url:
        logging.warning("No se encontró DISCORD_WEBHOOK en el entorno. No se envía a Discord.")
        return

    payload = {
        "content": f"```{mensaje}```"  # Formato de bloque de código en Discord
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            logging.warning(f"Error al enviar a Discord: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Excepción al enviar a Discord: {e}")
