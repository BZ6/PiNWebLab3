from fastapi import APIRouter, HTTPException, status
import requests


router = APIRouter(prefix="/parser", tags=["parser"])


@router.post("/")
def parse_site(url: str):
    try:
        response = requests.post("http://parser:8000/parse",
                                 json={"url": url})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
