from fastapi import FastAPI
from ddtrace import patch_all
import ddtrace
import logging

patch_all()
ddtrace.config.service = "service-d"
ddtrace.config.env = "local"

logging.basicConfig(
    filename="/home/ajay/proj/dd_app/dd_app_2/service-d/service-d.log",  # <-- must match the path in conf.yaml
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [service-d] %(message)s"
)

#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [service-d] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/final")
def final_response():
    logger.info("Received request at /final")
    return {"message": "Hello from Service D"}

