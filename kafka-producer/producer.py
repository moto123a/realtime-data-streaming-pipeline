from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ["P-100", "P-200", "P-300", "P-400"]
customers = ["C-1", "C-2", "C-3", "C-4", "C-5"]

while True:
    event = {
        "event_time": datetime.utcnow().isoformat(),
        "order_id": f"O-{random.randint(100000,999999)}",
        "customer_id": random.choice(customers),
        "product_id": random.choice(products),
        "qty": random.randint(1,5),
        "unit_price": round(random.uniform(50,250),2)
    }
    event["total_amount"] = event["qty"] * event["unit_price"]

    producer.send("orders-topic", event)
    print("[Producer] Sent:", event)

    time.sleep(1)

