import websocket
#bitstamp
import ssl
import json
import bitstamp.client

import credencials

def client():
    return bitstamp.client.Trading(
        username = credencials.USERNAME, key = credencials.KEY, secret = credencials.SECRET)

def buy(qntd):
    trading_client = client()
    trading_client.buy_market_order(qntd)

def sell(qntd):
    trading_client = client()
    trading_client.sell_market_order(qntd)

def ao_abrir(ws):
    print('Open man!')

    json_subscribe = """ {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""
    ws.send(json_subscribe)

def ao_fechar(ws):
    print('Close man!')

def erro(ws, error):
    print('error man')
    print(error)

def ao_message(ws, message):
    message = json.loads(message)
    print('New message!')
    price = message['data']['price']
    print('The price is: BIT', price)

    if price > 9000:
        sell()
    elif price < 8000:
        buy()
    else:
        print('Wait for!')

if __name__ == '__main__':
        #print('its works man')
        #websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                    #on_open=ao_abrir())
                                    on_open=ao_abrir,
                                    on_close=ao_fechar,
                                    on_message=ao_message,
                                    on_error=erro)

        #ws.run_forever()
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})