from aiogram.filters.command import Command
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    user = message.from_user
    # chat_id = message.chat.id

    # Извлекаем данные о пользователе
    user_id = user.id
    username = user.username
    first_name = user.first_name
    last_name = user.last_name

    # Формируем ответное сообщение с данными
    response = (
        f"Привет, {first_name}!\n\n"
        f"Ваши данные:\n"
        f"ID: {user_id}\n"
        f"Username: @{username}\n"
        f"Имя: {first_name}\n"
        f"Фамилия: {last_name or 'Не указана'}\n\n"
        # f"Chat id беседы: {chat_id}"
    )

    # Отправляем сообщение пользователю
    await message.answer(response)
