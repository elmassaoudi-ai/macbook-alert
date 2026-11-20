import os
import requests

token = os.environ["TELEGRAM_TOKEN"]

r = requests.get(
    f"https://api.telegram.org/bot{token}/getMe"
)

print(r.text)

