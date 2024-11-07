from random import random

from aiogram import types, Dispatcher
from config import bot, dp
import os



async def start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'hello {message.from_user.first_name}\n'
                                f'Твой Telegram Id {message.from_user.id}')
    await message.answer('Helloo')

async def send_meme(message: types.Message):
    photo_path = os.path.join("media", "img.png")
    # photo = open(photo_path, "rb")

    with open(photo_path, "rb") as image:
        await message.answer_photo(photo=image,
                                   caption= 'meme')

async def send_photo(message: types.Message):
    photo_path=os.path.join("media", "img_1.png")

    with open(photo_path, "rb") as image:
        await message.answer_photo(photo=image,
                                   caption= 'photo')

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def send_game(message: types.Message):
    selected_game = random.choice(games)


    await bot.send_message(
        chat_id=message.chat.id,
        text=f"🎲 Ты подкинул кость! Игра: {selected_game}"
    )


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(send_meme, commands=['meme'])
    dp.register_message_handler(send_photo, commands=['photo'])
    dp.register_message_handler(send_game, commands=['game'])