from bs4 import BeautifulSoup
import requests

from src.connection import SessionLocal
from src.models import WebPage


def parse_and_save(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title'

        with SessionLocal() as session:
            page = WebPage(url=url, title=title)
            session.add(page)
            session.commit()
        print(f"Parsed: {url}: {title}")
    except Exception as e:
        print(f"Error parsing {url}: {e}")
