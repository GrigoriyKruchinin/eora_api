import json
import requests
from bs4 import BeautifulSoup
from app.config import settings


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}


def fetch_data_from_url(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find("h1").text.strip()

        return {"content": content, "url": url}
    except Exception as e:
        return {"error": f"Ошибка при парсинге данных: {e}"}


def fetch_all_data():
    all_data = []
    for url in settings.SOURCES_URLS:
        data = fetch_data_from_url(url)
        all_data.append(data)

    with open("data/parsed_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    return all_data


if __name__ == "__main__":
    fetch_all_data()
