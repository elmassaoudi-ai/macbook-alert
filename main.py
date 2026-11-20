import requests

url = "INTERNETSEITE DIE GECHECKT WERDEN SOLL"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

r = requests.get(url, headers=headers, timeout=30)

print("STATUS:", r.status_code)
print(r.text[:2000])

