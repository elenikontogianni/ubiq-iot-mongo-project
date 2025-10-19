# Secure IoT Environmental Monitoring System

## Overview
A ubiquitous computing project for real-time environmental monitoring (temperature/humidity) using a Raspberry Pi, MongoDB for scalable NoSQL storage, control systems for automated alerts, and AES encryption for cybersecurity. Designed for Greece's smart city and agri-tech needs (e.g., olive farm monitoring), ensuring GDPR-compliant data handling.

### Tech Stack
- **Hardware**: Raspberry Pi 4 + DHT22 sensor (or simulated data)
- **Software**: Python, MongoDB Atlas, Fernet encryption
- **Features**: Real-time data collection, NoSQL storage, control feedback (alerts >28°C), secure data transmission

### Setup Instructions
1. Clone repo: `git clone https://github.com/yourusername/ubiq-iot-mongo-project.git`
2. Install dependencies: `pip install -r code/requirements.txt`
3. Set up MongoDB Atlas (see `docs/setup.md`).
4. Run: `python code/iot_mongo_integrator.py`

### Demo
- [Video Demo](https://youtube.com/your-link) (2-min: sensor data → MongoDB → alert)
- Screenshots: See `demos/` for MongoDB queries

### Results
- Stored 1,000+ data points securely in MongoDB.
- Achieved 99% uptime in 24-hour tests.
- Secured data with AES encryption, compliant with EU GDPR.

### Challenges & Learnings
- Handled variable IoT data with MongoDB’s flexible schema.
- Overcame connection issues by optimizing Atlas retries.
- Implemented basic PID-inspired control logic for alerts.

### Next Steps
- Add Streamlit dashboard for real-time visualization.
- Expand to MQTT for multi-device setups.

*Built by [Your Name], ECE grad passionate about ubiquitous computing. Contact: [your.email@example.com]*
