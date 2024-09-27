import json
from aiogram.utils.markdown import hlink


def load_parsed_data(file_path: str) -> list:
    """
    Загрузка и парсинг данных из JSON файла.

    :param file_path: Путь к JSON файлу
    :return: Список с данными из файла
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            parsed_data = json.load(f)
        return parsed_data
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {file_path}: {e}")


def prepare_sources_data(parsed_data: list) -> str:
    """
    Формирование строки данных для использования в LLM на основе загруженного JSON.

    :param parsed_data: Список с данными
    :return: Строка данных, подготовленная для использования в LLM
    """
    sources_data = ""
    for item in parsed_data:
        sources_data += f"Название: {item['content']}, URL: [{item['url']}]\n"
    return sources_data


def replace_links_with_numbers(response: str, links: list) -> str:
    """
    Замена ссылок на порядковые номера с гиперссылками.

    :param response: Текст с исходными ссылками
    :param links: Список ссылок, найденных в тексте
    :return: Текст с заменёнными ссылками на номера
    """
    for i, link in enumerate(links, 1):
        clean_link = link[1:-1]
        response = response.replace(link, hlink(f"[{i}]", clean_link), 1)
    return response
