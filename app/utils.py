import json
from aiogram.utils.markdown import hlink


def load_parsed_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            parsed_data = json.load(f)
        return parsed_data
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {file_path}: {e}")


def prepare_sources_data(parsed_data):
    sources_data = ""
    for item in parsed_data:
        sources_data += f"Название: {item['content']}, URL: [{item['url']}]\n"
    return sources_data


def replace_links_with_numbers(response, links):
    for i, link in enumerate(links, 1):
        clean_link = link[1:-1]
        response = response.replace(link, hlink(f"[{i}]", clean_link), 1)
    return response
