from fastapi import FastAPI
import requests
from ddtrace import patch_all
import ddtrace
import logging
from fastapi.responses import HTMLResponse

patch_all()
ddtrace.config.service = "service-a"
ddtrace.config.env = "local"

logging.basicConfig(
    filename="/home/ajay/proj/dd_app/dd_app_2/service-a/service-a.log",  # <-- must match the path in conf.yaml
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [service-a] %(message)s"
)
#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [service-a] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/start")
def start_trace():
    logger.info("Received request at /start")
    response = requests.get("http://localhost:7001/process")
    logger.info("Forwarded request to service-b, received response")
    return {"message": "Started flow", "response": response.json()}

@app.get("/", response_class=HTMLResponse)
def home():
    return '''
<!DOCTYPE html>
<html>
<head><title>Microservices Tracing Demo</title></head>
<body>
    <h1>Trigger Trace Flow</h1>
    <button onclick="callService()">Start Flow</button>
    <pre id="output"></pre>
    <script>
        async function callService() {
            const response = await fetch('/start');
            const data = await response.json();
            document.getElementById('output').textContent = JSON.stringify(data, null, 2);
        }
    </script>
</body>
</html>
    '''

