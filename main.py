from decouple import config
from aiogram import Dispatcher, Bot, executor, types
import logging

token = config ('TOKEN')
bot = Bot (token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'hello {message.from_user.first_name}\n'
                                f'Твой Telegram Id {message.from_user.id}')
    await message.answer('Helloo')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)