import os
import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "✅ Testnachricht vom MacBook-Alarm"
    }
)

print(r.text)
