import json


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
