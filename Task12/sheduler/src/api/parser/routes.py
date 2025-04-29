from fastapi import APIRouter, HTTPException, status
from celery.result import AsyncResult
from asyncio import sleep

from src.task import parse_url


router = APIRouter(prefix="/parser", tags=["parser"])


@router.post("/")
async def parse_site(url: str):
    try:
        task = parse_url.apply_async((url,))
        result = AsyncResult(task.id)

        # Не хочу писать еще один эндпоинт который показывает статус
        # таски, поэтому пусть таска поспит пока не подойдет ее очередь
        while not result.ready():
            await sleep(1)

        if not result.successful():
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result.result)
        
        return result.result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
