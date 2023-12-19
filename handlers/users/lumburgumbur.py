from aiogram import types
from loader import dp


@dp.message_handler(commands=["ABOUT"])
async def about_lamborghini(message: types.Message):
    if "Lamborghini" in message.text:
        text = "Automobili Lamborghini SpA (italyancha talaffuzi:  [autoˈmɔːbili lamborˈɡiːni]) — eng mashhur italyan avtomobil ishlab chiqaruvchilaridan biri hisoblanadi. Uning bosh qarorgohi SantʼAgata Bolonez shahrida joylashgan. U qimmat va hashamatli avtomobillardan tashqari sport avtomobillar ishlab chiqarish bilan ham shugʻullanadi. Kompaniya oʻzining shoʻba korxonasi Audi orqali Volkswagen guruhiga tegishli."
        await message.answer(text)


# @dp.message_handler(commands="TYPES OF LAMBORGHINI")
# async def about_lambos(message: types.Message):


