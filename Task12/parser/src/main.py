from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import requests

from src.parse_and_save import parse_and_save
from src.connection import init_db


app = FastAPI()

class ParseRequest(BaseModel):
    url: str

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/parse")
def parse(request: ParseRequest):
    try:
        response = requests.get(request.url)
        response.raise_for_status()
        parse_and_save(request.url)
        return {"message": "Parsing completed"}
    except requests.RequestException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
