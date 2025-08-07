from fastapi import FastAPI
import requests
from ddtrace import patch_all
import ddtrace
import logging

patch_all()
ddtrace.config.service = "service-c"
ddtrace.config.env = "local"

logging.basicConfig(
    filename="/home/ajay/proj/dd_app/dd_app_2/service-c/service-c.log",  # <-- must match the path in conf.yaml
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [service-c] %(message)s"
)

#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [service-c] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/data")
def get_data():
    logger.info("Received request at /data")
    response = requests.get("http://localhost:6003/final")
    logger.info("Forwarded request to service-d, received response")
    return {"message": "Data from C", "response": response.json()}

