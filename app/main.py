import re
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config import settings
from app.gpt import gpt_client
from app.utils import replace_links_with_numbers


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот, который может отвечать на вопросы с использованием данных с сайта EORA и YandexGPT."
    )


@dp.message()
async def handle_message(message: types.Message):
    response = gpt_client.generate_response(message.text)
    links = re.findall(r"\[https?://[^\]]+\]", response)
    response = replace_links_with_numbers(response, links)

    await message.reply(response, parse_mode="HTML")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
