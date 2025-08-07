from fastapi import FastAPI
import requests
from ddtrace import patch_all
import ddtrace
import logging

patch_all()
ddtrace.config.service = "service-b"
ddtrace.config.env = "local"

logging.basicConfig(
    filename="/home/ajay/proj/dd_app/dd_app_2/service-b/service-b.log",  # <-- must match the path in conf.yaml
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [service-b] %(message)s"
)

#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [service-b] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/process")
def process_data():
    logger.info("Received request at /process")
    response = requests.get("http://localhost:6002/data")
    logger.info("Forwarded request to service-c, received response")
    return {"message": "Processed in B", "response": response.json()}

