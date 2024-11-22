from aiogram import executor, types
from config import dp, admin, bot
import logging
from handlers import commands, quiz,game, store, echo



commands.register_commands(dp)
quiz.register_handler_quiz(dp)
game.register_game(dp)
store.register_store(dp)
echo.register_echo(dp)

async def on_startup(_):
    await bot.send_message(
        text ='bot is started',
        chat_id= admin
    )

async def on_shut(_):
    await bot.send_message(
        text ='bot is turned off',
        chat_id= admin
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
    on_shutdown=on_shut)

