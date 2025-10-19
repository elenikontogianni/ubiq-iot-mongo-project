import random  # For simulation; replace with Adafruit_DHT for Raspberry Pi
from datetime import datetime

def read_sensor():
    # For hardware: Uncomment and use DHT22 on GPIO pin 4
    # import Adafruit_DHT
    # DHT_SENSOR = Adafruit_DHT.DHT22
    # DHT_PIN = 4
    # humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    # if humidity is not None and temperature is not None:
    #     return {"temperature": temperature, "humidity": humidity, "timestamp": datetime.utcnow().isoformat()}
    # Simulate data for no hardware
    return {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 70),
        "timestamp": datetime.utcnow().isoformat()
    }
