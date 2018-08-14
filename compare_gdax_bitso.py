import websocket
import json
import threading
import requests

BTC = 'USD', 'EUR', 'GBP'
ETH = 'BTC', 'USD', 'EUR'

url = 'wss://ws-feed.gdax.com'

gdax_ws = websocket.create_connection(url)
gdax_ws.connect(url)

tickers = {}

product_ids = ['LTCBTC', 'LTCUSD', 'LTCEUR', 'ETHBTC', 'ETHUSD', 'ETHEUR', 'BTCUSD', 'BTCEUR', 'BTCGBP', 'BCHBTC', 'BCHUSD', 'BCHEUR']

def get_product_ids():
    btc = ['BTC-'+i for i in BTC]
    eth = ['ETH-'+i for i in ETH]
    bch = ['BCH-'+i for i in ETH]
    ltc = ['LTC-'+i for i in ETH]
    return  btc + eth + bch + ltc

def get_ticker_wss():
    while True:
        x = json.loads(gdax_ws.recv())
        if 'type' in x and x['type'] == 'ticker':
            tickers[''.join(x['product_id'].split('-'))] = x

def init_all_tickers():
    product_ids = get_product_ids()
    data = {'type':'subscribe', 'channels':[{"name":"ticker", "product_ids":product_ids}]}
    gdax_ws.send(json.dumps(data))
    threading.Thread(target=get_ticker_wss).start()
    while len(tickers) < len(product_ids):
        pass
    
def compare_bitso_gdax():
    payload = requests.get('https://api.bitso.com/v3/ticker/').json()['payload']
    for i in payload:
        base, quote = i['book'].split('_')
        if quote != 'mxn' or base == 'xrp' or base == 'tusd':
            continue
        bitso = float(i['last'])
        gdax = float(tickers[base.upper()+'USD']['price'])
        print(base.upper(), '\t',bitso, '\t',gdax, '\t',bitso/gdax)
        print('')

if __name__ == '__main__':
    init_all_tickers()
