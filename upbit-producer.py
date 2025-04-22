from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',
}
p = Producer(conf)

p.poll(0)
p.produce('temp', 'python-message-test')
p.flush()