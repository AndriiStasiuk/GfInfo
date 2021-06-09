from os import environ

SERVICE_NAME = "gw_info"
LOG_SERVICE_NAME = "service_name"
API_PREFIX = f"/{SERVICE_NAME}/v1"
DB_URL = f"postgresql://{environ['DB_USER']}:{environ['DB_PASSWORD']}@{environ['DB_HOST']}:{environ['DB_PORT']}/gw_info"
