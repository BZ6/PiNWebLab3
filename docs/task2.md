# Подзадача 2: Вызов парсера из FastAPI

**Эндпоинт в FastAPI для вызова парсера**:
Необходимо добавить в FastAPI приложение ендпоинт, который будет принимать запросы с URL для парсинга от клиента, отправлять запрос парсеру (запущенному в отдельном контейнере) и возвращать ответ с результатом клиенту.

```python
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
```

Тут нужно обратить внимание на хоста в URL, так как мы используем docker-compose, то
создается сеть и тогда можно обращаться прямо по адресу сервиса (parser). В дальнейшем
специально буду указывать название сети в docker-compose, хотя они на самом деле и без
меня объединяются в сеть.
