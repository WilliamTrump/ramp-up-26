from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

CHANNEL = "messages"

class PublishRequest(BaseModel):
    text: str

@app.post("/publish")
def publish(request: PublishRequest):
    redis_client.publish(CHANNEL, request.text)
    return {
        "status": "published",
        "message": request.text,
        "channel": CHANNEL
    }