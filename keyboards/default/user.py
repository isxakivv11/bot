from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Telefon raqamni jo'matish", request_contact=True)
    ]], resize_keyboard=True
)


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="ABOUT Lamborghini🏎️")
    ]], resize_keyboard=True
)