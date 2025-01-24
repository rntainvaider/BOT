from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers import start
from config import API_TOKEN
from utils.log import setup_logging
import asyncio
import logging


async def main():
    # Объект бота
    bot = Bot(token=API_TOKEN)
    # Связывает bot с обработчиками событий
    dp = Dispatcher()

    # Регистрируем обработчики из других файлов
    dp.include_router(start.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    # Настройка логирования
    setup_logging()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
