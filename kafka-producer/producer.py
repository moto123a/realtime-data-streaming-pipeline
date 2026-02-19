from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

origins = ["Chicago Rail Yard", "Dallas Hub", "Houston Freight Port", "Denver Depot"]
destinations = ["Atlanta Terminal", "Seattle Hub", "Phoenix Yard", "Miami Freight Station"]
transport_modes = ["Rail", "Truck"]
shipment_status = ["In Transit", "Delayed", "Delivered", "At Warehouse"]

while True:
    shipment_event = {
        "shipment_id": f"SHP-{random.randint(10000,99999)}",
        "origin": random.choice(origins),
        "destination": random.choice(destinations),
        "transport_mode": random.choice(transport_modes),
        "shipment_status": random.choice(shipment_status),
        "weight_tons": random.randint(10,100),
        "distance_km": random.randint(100,2000),
        "event_timestamp": datetime.utcnow().isoformat()
    }

    producer.send("shipment_events", shipment_event)
    print("[Shipment Producer] Sent:", shipment_event)

    time.sleep(1)
