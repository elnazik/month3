from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from random import choice


async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)