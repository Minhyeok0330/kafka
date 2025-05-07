from confluent_kafka import Producer
import time
import requests
import json

UPBIT_URL = 'https://api.upbit.com/v1/ticker'
params = {
    'markets': 'KRW-BTC'
}

conf = {
    'bootstrap.servers': 'localhost:9092',
}
p = Producer(conf)

while True:
    res = requests.get(UPBIT_URL, params=params)
    bit_data = res.json()[0]
    json_data = json.dumps(bit_data)
    print(json_data)
    #result = f"{bit_data['market']}, {bit_data['trade_date']}, {bit_data['trade_time']}, {bit_data['trade_price']}"
    p.poll(0)
    p.produce('bitcoin', json_data)
    p.flush()
    
    time.sleep(5)
    