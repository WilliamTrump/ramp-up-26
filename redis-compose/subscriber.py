import redis

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

pubsub = redis_client.pubsub()
CHANNEL = "messages"

pubsub.subscribe(CHANNEL)

print(f"Listening on channel: {CHANNEL}")
for message in pubsub.listen():
    if message["type"] == "message":
        print(message["data"], flush=True)