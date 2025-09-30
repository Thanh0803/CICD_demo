from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SumIn(BaseModel):
    a: float
    b: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sum")
def sum_numbers(body: SumIn):
    return {"sum": body.a + body.b}