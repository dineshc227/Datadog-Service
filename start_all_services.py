import subprocess
import os
import time

# Define microservices and their ports
services = [
    {"name": "service-d", "port": 6003},
    {"name": "service-c", "port": 6002},
    {"name": "service-b", "port": 6001},
    {"name": "service-a", "port": 7001},
]

processes = []

print("🚀 Starting all services...")

for service in services:
    path = os.path.abspath(service["name"])
    cmd = [os.path.join(os.environ['VIRTUAL_ENV'], "bin", "python"), "-m", "uvicorn", "app:app", "--port", str(service["port"]), "--reload"]
    process = subprocess.Popen(cmd, cwd=path)
    processes.append((service["name"], process))
    print(f"✅ Started {service['name']} on port {service['port']}")
    time.sleep(1)

print("\n🌐 Visit http://localhost:5000 to trigger the flow")
print("🛑 Press Ctrl+C to stop all services")

try:
    for _, process in processes:
        process.wait()
except KeyboardInterrupt:
    print("\n⚠️ Stopping all services...")
    for name, process in processes:
        process.terminate()
        print(f"🛑 Terminated {name}")

