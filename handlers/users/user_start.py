from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import user_main_menu
from loader import dp
from states.user import RegisterState
from utils.db_api.user_commands import get_user


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    user = await get_user(chat_id=message.chat.id)
    if user:
        text = "Xush kelibsiz"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Iltimos ismingiz kiriting"
        await RegisterState.full_name.set()
        await message.answer(text=text)







