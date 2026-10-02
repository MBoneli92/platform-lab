import os
from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()
REQUESTS = Counter("app_requests_total", "Total requests", ["endpoint"])

@app.get("/")
def root():
    REQUESTS.labels(endpoint="/").inc()
    return {"app": "platform-lab", "version": os.getenv("APP_VERSION", "dev")}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)