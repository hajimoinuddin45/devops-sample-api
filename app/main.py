import signal
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from app.logger import get_logger

logger = get_logger()
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def home():
    logger.info("GET / called")
    return {"message": "API running successfully"}

@app.post("/items")
def create_item(item: Item):
    logger.info(f"POST /items with {item}")
    return {"item": item}

@app.get("/health")
def health():
    return {"status": "ok"}

def shutdown_handler(sig, frame):
    logger.info("Shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)
