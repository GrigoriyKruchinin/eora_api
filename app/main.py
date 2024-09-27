import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import settings
from app.gpt import gpt_client


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

with open("data/parsed_data.json", "r", encoding="utf-8") as f:
    parsed_data = json.load(f)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот, который может отвечать на вопросы с использованием данных с сайта EORA и YandexGPT."
    )


@dp.message()
async def handle_message(message: types.Message):
    question = message.text
    context = "\n".join([item["content"] for item in parsed_data])
    prompt = f"Вопрос: {question}\nКонтекст: {context}"
    response = gpt_client.generate_response(prompt)

    await message.reply(response)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
