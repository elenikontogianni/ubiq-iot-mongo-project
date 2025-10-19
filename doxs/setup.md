# Setup Guide
1. Hardware: Raspberry Pi 4, DHT22 on GPIO 4 (or simulate in `sensor_reader.py`).
2. MongoDB Atlas: Create free cluster, add `iot_db`/`environmental_data`, update connection string in `iot_mongo_integrator.py`.
3. Install Python 3.9+, Git.
4. Run `pip install -r code/requirements.txt`.
5. Start: `python code/iot_mongo_integrator.py`.
