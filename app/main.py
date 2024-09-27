import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import settings
from app.gpt import gpt_client


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот, который может отвечать на вопросы с использованием данных с сайта EORA и YandexGPT."
    )


import re
from aiogram.utils.markdown import hlink


@dp.message()
async def handle_message(message: types.Message):
    question = message.text
    context = "\n".join(
        [f"{item['content']} [{item['url']}]" for item in settings.PARSED_DATA]
    )
    prompt = f"Вопрос: {question}\nКонтекст: {context}"
    response = gpt_client.generate_response(prompt)

    links = re.findall(r"\[https?://[^\]]+\]", response)

    for i, link in enumerate(links, 1):
        clean_link = link[1:-1]
        response = response.replace(link, hlink(f"[{i}]", clean_link), 1)

    await message.reply(response, parse_mode="HTML")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
