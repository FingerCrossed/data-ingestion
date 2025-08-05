import json
import os
import time
from kafka import KafkaProducer

# ====== Configuration ======
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC_NAME = "supply_chain_sales"

# ====== Initialize Kafka Producer ======
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=3
)

# ====== Simulate Sample Data (e.g. from S3) ======
sample_data = [
    {
        "market": "Japan",
        "order_id": "JP001",
        "product_code": "A123",
        "amount": 100,
        "order_date": "2025-08-04"
    },
    {
        "market": "Japan",
        "order_id": "JP002",
        "product_code": "B456",
        "amount": 200,
        "order_date": "2025-08-04"
    }
]
# ====== Log ingestion status ======
def log_ingestion(record, status, error_msg=None):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "market": record.get("market"),
        "order_id": record.get("order_id"),
        "status": status,  # "SUCCESS" or "FAILURE"
        "error": error_msg or ""
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"Ingestion Log: {log_entry}")
    
# ====== Send Messages to Kafka ======
for record in sample_data:
    try:
        producer.send(TOPIC_NAME, value=record)
        print(f"Sent record: {record}")
        time.sleep(0.2)
    except Exception as e:
        print(f"Failed to send record: {record}")
        print(f"Error: {str(e)}")

producer.flush()
producer.close()
