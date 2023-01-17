from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello mate"}
    

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}