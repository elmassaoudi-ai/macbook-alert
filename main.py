import requests

url = "https://www.amazon.de/s?k=macbook&i=warehouse-deals&srs=3581963031"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status:", r.status_code)
print(r.text[:500])
