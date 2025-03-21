import psutil
import subprocess
import time

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=5)
    print(f"Current CPU Usage: {cpu_usage}%")
    if cpu_usage > 75:
        print("🚀 CPU Usage High! Triggering Auto-Scaling on GCP...")
        subprocess.run([
            "gcloud", "compute", "instances", "start", "my-cloud-vm",
            "--zone=us-central1-b"
        ])

while True:
    check_cpu()
    time.sleep(10)
