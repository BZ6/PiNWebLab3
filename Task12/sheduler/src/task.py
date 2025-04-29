import requests

from src.celery_config import app


@app.task
def parse_url(url: str):
    response = requests.post("http://parser:8000/parse",
                             json={"url": url})
    response.raise_for_status()
    return response.json()
