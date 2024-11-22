from aiogram import types, Dispatcher
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from config import bot



from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class Store(StatesGroup):
    name= State()
    size= State()
    category= State()
    price= State()
    photo= State()

async def start_fsm(message: types.Message):
    await message.answer('Name of product?')
    await Store.name.set()

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        kb = types.ReplyKeyboardMarkup()
        b1 = types.KeyboardButton(text = 'L')
        b2 = types.KeyboardButton(text='S')
        b3 = types.KeyboardButton(text='M')
        kb.add(b1, b2, b3)
        await message.answer('What is the size?',
        reply_markup=kb)
        await Store.next()

async def process_size(message:types.Message, state: FSMContext):
    kb= types.ReplyKeyboardMarkup()
    if message.text in ['S', 'M', 'L']:
        async with state.proxy() as data:
            data['size'] = message.text
        await message.answer('category of product?', reply_markup=kb)
        await Store.next()
    else:
        await message.answer('Press only bottons!!!',)

async def process_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Price of product?',)
    await Store.next()

async def process_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer('send a photo of product?',)
    await Store.next()

async def process_photo(message: types.Message,
state: FSMContext):
     photo = message.photo[-1].file_id
     async with state.proxy() as data:
         await message.answer_photo(
             photo= photo,
             caption=f"{data['name']}\n"
                     f"{data['size']}\n"
                     f"{data['category']}\n"
                     f"{data['price']}"
             )
         await state.finish()


def register_store(dp:Dispatcher):
    dp.register_message_handler(start_fsm, commands= 'Store')
    dp.register_message_handler(process_name, state='Store.name')
    dp.register_message_handler(process_size, state='Store.size')
    dp.register_message_handler(process_category, state='Store.category')
    dp.register_message_handler(process_price, state='Store.price')
    dp.register_message_handler(process_photo, state='Store.photo')