import requests
def send_request():
    params = {"market": "BTCUSDT", "limit": 100, "type": "1day"}
    response = requests.get("https://api.coinex.com/v1/market/kline",params = params)
    if response.status_code == 200:
        data = response.json()
        print(data["title"])
    else:
        print("Error", response.status_code)

send_request()
