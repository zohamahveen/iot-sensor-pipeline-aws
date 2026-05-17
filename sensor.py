import time
import json
import random
from awscrt import mqtt
from awsiot import mqtt_connection_builder

# Configuration
ENDPOINT = "ax67jx1xxroii-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "temperature-voltage-sensor"
TOPIC = "sensor/data"
CERT_DIR = "C:\\Users\\Zohas\\OneDrive\\Desktop\\zoha\\AWS\\AWS PROJECTS\\PROJECT-3\\certificates\\"

# Certificate file names - update these to match your exact filenames
CERT_FILE = CERT_DIR + "76f8443d6890f095f8f093e13d0f996c172f2224a2587e55bde51eb14ae7c2eb-certificate.pem.crt"
KEY_FILE = CERT_DIR + "76f8443d6890f095f8f093e13d0f996c172f2224a2587e55bde51eb14ae7c2eb-private.pem.key"
ROOT_CA = CERT_DIR + "AmazonRootCA1.pem"

# Build MQTT connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=CERT_FILE,
    pri_key_filepath=KEY_FILE,
    ca_filepath=ROOT_CA,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

print("Connecting to IoT Core...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("Connected!")

# Simulate sensor readings
try:
    while True:
        temperature = round(random.uniform(20.0, 100.0), 2)
        voltage = round(random.uniform(210.0, 240.0), 2)
        
        payload = {
            "device_id": "sensor-001",
            "temperature": temperature,
            "voltage": voltage,
            "timestamp": int(time.time())
        }
        
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(payload),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        
        print(f"Published: {payload}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Disconnecting...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected.")