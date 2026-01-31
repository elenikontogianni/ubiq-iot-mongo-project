from pymongo import MongoClient
from cryptography.fernet import Fernet
import time
from sensor_reader import read_sensor

# MongoDB setup
client = MongoClient("your_mongodb_atlas_connection_string")  # Replace with yours
db = client.iot_db
collection = db.environmental_data

# Encryption setup
key = Fernet.generate_key()  # In prod: Store securely
cipher = Fernet(key)

def control_logic(data):
    if data["temperature"] > 28:
        print("ALERT: High temp! Activating cooling...")
        return {"alert": True, "action": "cooling_on"}
    return {"alert": False}

while True:
    raw_data = read_sensor()
    if raw_data:
        control_result = control_logic(raw_data)
        full_data = {**raw_data, **control_result, "device_id": "pi_01"}
        # Encrypt sensitive data
        full_data["encrypted_payload"] = cipher.encrypt(str(full_data).encode()).decode()
        collection.insert_one(full_data)
        print(f"Inserted: {full_data}")
    time.sleep(5)  # Collect every 5 sec
