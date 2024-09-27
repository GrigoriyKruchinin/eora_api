import os
from dotenv import load_dotenv
from app.utils import load_parsed_data, prepare_sources_data

load_dotenv()


class Settings:
    # Ваши переменные окружения
    YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

    # Путь к файлу с данными
    PARSED_DATA_FILE_PATH = "data/parsed_data.json"

    # Чтение и подготовка данных
    PARSED_DATA = load_parsed_data(PARSED_DATA_FILE_PATH)
    SOURCES_DATA = prepare_sources_data(PARSED_DATA)

    # Контекст для GPT
    LLM_CONTEXT = (
        "Ты являешься консультантом для ответов на вопросы наших потенциальных клиентов! "
        "Твоя задача — давать краткие и чёткие ответы на основе данных из кейсов компании. "
        "В каждом ответе используй не более 1-3 примеров из ниже приведенных данных, оформляя их в виде нумерованного списка. "
        "Структура ответа должна всегда быть следующей:\n"
        "1. Указать, что ты можешь предложить клиенту.\n"
        "2. Перечислить примеры в формате: 1. Название кейса и короткое описание (в скобках укажи URL на проект).\n"
        "Пример структуры ответа:\n"
        "- Вопрос: Что вы можете сделать для ритейлеров?\n"
        "- Ответ: Мы можем создать различные решения для ритейлеров. Вот несколько примеров, которые уже реализованы нами:\n"
        "1. Бот для HR для компании «Магнит», который автоматически приглашает кандидатов на собеседование "
        "[https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie].\n"
        "2. Система распознавания химических схем для автоматизации производственных процессов "
        "[https://eora.ru/cases/chemrar-raspoznovanie-molekul].\n"
        "3. Нейросеть для определения веса блюд по фото, которая поможет автоматизировать работу кафе и ресторанов "
        "[https://eora.ru/cases/ifarm-nejroset-dlya-ferm].\n"
        "Делай ответы краткими, по существу, всегда соблюдай формат нумерованного списка и включай ссылки на проекты.\n"
        "Вот примеры данных, которые ты можешь использовать в своих ответах:\n"
    ) + SOURCES_DATA

    # Ссылки на кейсы компании для формирования контекста GPT
    SOURCES_URLS = [
        "https://eora.ru/cases/promyshlennaya-bezopasnost",
        "https://eora.ru/cases/lamoda-systema-segmentacii-i-poiska-po-pohozhey-odezhde",
        "https://eora.ru/cases/navyki-dlya-golosovyh-assistentov/karas-golosovoy-assistent",
        "https://eora.ru/cases/assistenty-dlya-gorodov",
        "https://eora.ru/cases/avtomatizaciya-v-promyshlennosti/chemrar-raspoznovanie-molekul",
        "https://eora.ru/cases/zeptolab-skazki-pro-amnyama-dlya-sberbox",
        "https://eora.ru/cases/goosegaming-algoritm-dlya-ocenki-igrokov",
        "https://eora.ru/cases/dodo-pizza-robot-analitik-otzyvov",
        "https://eora.ru/cases/ifarm-nejroset-dlya-ferm",
        "https://eora.ru/cases/zhivibezstraha-navyk-dlya-proverki-rodinok",
        "https://eora.ru/cases/sportrecs-nejroset-operator-sportivnyh-translyacij",
        "https://eora.ru/cases/avon-chat-bot-dlya-zhenshchin",
        "https://eora.ru/cases/computer-vision/iss-analiz-foto-avtomobilej",
        "https://eora.ru/cases/purina-master-bot",
        "https://eora.ru/cases/skinclub-algoritm-dlya-ocenki-veroyatnostej",
        "https://eora.ru/cases/skolkovo-chat-bot-dlya-startapov-i-investorov",
        "https://eora.ru/cases/purina-podbor-korma-dlya-sobaki",
        "https://eora.ru/cases/purina-navyk-viktorina",
        "https://eora.ru/cases/dodo-pizza-pilot-po-avtomatizacii-kontakt-centra",
        "https://eora.ru/cases/dodo-pizza-avtomatizaciya-kontakt-centra",
        "https://eora.ru/cases/icl-bot-sufler-dlya-kontakt-centra",
        "https://eora.ru/cases/s7-navyk-dlya-podbora-aviabiletov",
        "https://eora.ru/cases/workeat-whatsapp-bot",
        "https://eora.ru/cases/absolyut-strahovanie-navyk-dlya-raschyota-strahovki",
        "https://eora.ru/cases/kazanexpress-poisk-tovarov-po-foto",
        "https://eora.ru/cases/kazanexpress-sistema-rekomendacij-na-sajte",
        "https://eora.ru/cases/intels-proverka-logotipa-na-plagiat",
        "https://eora.ru/cases/karcher-viktorina-s-voprosami-pro-uborku",
        "https://eora.ru/cases/chat-boty/purina-friskies-chat-bot-na-sajte",
        "https://eora.ru/cases/nejroset-segmentaciya-video",
        "https://eora.ru/cases/chat-boty/essa-nejroset-dlya-generacii-rolikov",
        "https://eora.ru/cases/qiwi-poisk-anomalij",
        "https://eora.ru/cases/frisbi-nejroset-dlya-raspoznavaniya-pokazanij-schetchikov",
        "https://eora.ru/cases/skazki-dlya-gugl-assistenta",
        "https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie",
    ]


settings = Settings()
