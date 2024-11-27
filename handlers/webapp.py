from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)

    instagram= KeyboardButton ('Instagram', web_app=WebAppInfo(url='https://www.instagram.com/'))
    youtube = KeyboardButton ('YouTube', web_app=WebAppInfo(url='https://www.youtube.com/'))
    netflix = KeyboardButton(text='Netflix', web_app=WebAppInfo(url='https://www.netflix.com/kg-ru/'))

    keyboard.add(instagram, youtube, netflix)

    await message.answer(text='WebApp кнопки', reply_markup=keyboard)


async def Inline_WebApp(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)


    instagram = InlineKeyboardButton('Instagram', web_app=WebAppInfo(url='https://www.instagram.com/'))
    youtube= InlineKeyboardButton('YouTube', web_app=WebAppInfo(url='https://www.youtube.com/'))
    netflix= InlineKeyboardButton('Netflix', web_app=WebAppInfo(url='https://www.netflix.com/kg-ru/'))

    keyboard.add(instagram, youtube, netflix)

    await message.answer(text= 'WebApp кнопки', reply_markup=keyboard)

def register_webapp_handlers(dp: Dispatcher):
    dp.register_message_handler(reply_webapp,commands='webapp_r')
    dp.register_message_handler(Inline_WebApp,commands='webapp_i')
