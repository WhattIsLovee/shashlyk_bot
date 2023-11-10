from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Dispatcher

import keyboard as kb


router = Router()
dp = Dispatcher()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer("Я могу помочь Вам при решении шашлычных вопросов.")

@dp.message
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
        )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)