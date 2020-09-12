from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []


class PayloadText(BaseModel):
    text: str


class Sender(BaseModel):
    phone: str
    name: str
    country_code: str
    dial_code: str


class Payload(BaseModel):
    id: str
    source: int
    payload: PayloadText
    sender: Sender


class Message(BaseModel):
    app: str
    timestamp: int
    version: int
    type: str
    payload: Payload


@app.post('/webhook/')
async def index(message: Message):
    return message
