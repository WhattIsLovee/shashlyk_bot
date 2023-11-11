from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Dispatcher

import keyboard as kb

import constants


router = Router()
dp = Dispatcher()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Я могу помочь Вам при решении шашлычных вопросов.')
    #await msg.answer(MENU, reply_markup=kb.exit_kb)

@router.message(F.text == 'Галерея')
async def galery_handler(msg: Message):
    await msg.answer(constants.GALLERY, reply_markup=kb.gallery_kb)


#@router.message(F.text == "Меню")
#async def menu(msg: Message):
    #await msg.answer(MENU, reply_markup=kb.exit_kb)