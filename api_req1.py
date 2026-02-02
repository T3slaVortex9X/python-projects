import requests
def send_request():
    params = {"market": "BTCUSDT", "limit": 10, "type": "1day"}
    response = requests.get("https://api.coinex.com/v1/market/kline",params = params)
    jsonrespon = response.json()

    print(jsonrespon)
send_request()