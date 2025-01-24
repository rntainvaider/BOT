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
    # # Влючаем логирование, чтобы не пропускать важных сообщений и запись в файл
    # logging.basicConfig(
    #     # filename="app.log",
    #     level=logging.INFO,
    #     # format="%(asctime)s - %(levelname)s - %(message)s",
    # )
    # Настройка логирования
    setup_logging()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
