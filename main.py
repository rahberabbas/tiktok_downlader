import requests
headers = {
        "method": "GET",
        "accept-encoding": "utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
r = requests.get('https://qload.info/', headers=headers)
print(r.status_code)