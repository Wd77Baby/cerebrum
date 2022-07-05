import os
import uuid


DEFAULT_HOST_MQTT = "106.15.193.98"
DEFAULT_HOST_REDIS = "106.15.193.98"
DEFAULT_CLOUD_URL = "http://106.15.193.98:8888"
DELIMITER = "/"

redis = {
    "host": os.getenv("redis_host") or DEFAULT_HOST_REDIS,
    "port": 6379,
    "password": "redis12345",
    "db": 1,
}

mqtt = {
    "host": os.getenv("mqtt_host") or DEFAULT_HOST_MQTT,
    "port": 1883,
    "client_id": uuid.uuid4().hex,
    "username": "root",
    "password": "abc@1234",
}

cloud_server = os.getenv("cloud_url") or DEFAULT_CLOUD_URL