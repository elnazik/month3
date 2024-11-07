from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot



async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Далее', callback_data='quiz_2')

    keyboard.add(button)

    question = 'where ara u from ?'

    answer = ['Bishkek', 'Moskow', 'Tokyo', 'Tashkent']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='саткын!!!',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Далее', callback_data='quiz_3')

    keyboard.add(button)

    question = 'Выбери страну ?'

    answer = ['Казахстан', 'Россия', 'Кыргызстан', 'Китай']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='не родной!!!',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)

        button = InlineKeyboardButton('завершить викторину', callback_data='end quiz')

        keyboard.add(button)

        question = 'какую форму имеет выше нарисованный предмет ?'

        answer = ['круг', 'квадрат', 'овал', 'треугольник']

        await bot.send_poll(
            chat_id=call.from_user.id,
            question=question,
            options=answer,
            is_anonymous=True,
            type='quiz',
            correct_option_id=0,
            explanation='не правильно!!!',
            open_period=60,
            reply_markup=keyboard
        )

def register_handler_quiz(dp: Dispatcher):
        dp.register_message_handler(quiz_1, commands=['quiz'])
        dp.register_callback_query_handler(quiz_2, text='quiz_2')
        dp.register_callback_query_handler(quiz_3, text='quiz_3')