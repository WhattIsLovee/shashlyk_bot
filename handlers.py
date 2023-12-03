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
    await msg.answer('Я могу помочь Вам при решении шашлычных вопросов.', reply_markup = kb.menu_kb)
    await msg.answer(constants.MENU, reply_markup=kb.menu_kb)


@router.message(F.text == constants.MENU)
async def menu(msg: Message):
    await msg.answer('👀 Куда теперь?', reply_markup = kb.menu_kb)


@router.message(F.text == constants.PICKLE_GUIDE)
async def pickle_handler(msg: Message):
    await msg.answer('•🫙 Маринады – подобранные ботом рецепты\
                                            •📒 Мои рецепты – записать свои рецепты\
                                            •⭐️ Избранное – Ваши любимые рецепты от бота', reply_markup = kb.pickle_kb) 
    #Пробелы нужны для ровного расположения пунктов в сообщении от бота.


@router.message(F.text == constants.FRYING_GUIDE)
async def pickle_handler(msg: Message):
    await msg.answer('•🪵 Гайды по жарке – подобранные ботом рецепты\
                                           •📒 Мои гайды – записать свои гайды\
                                                    •⭐️ Избранное – Ваши любимые рецепты от бота', reply_markup = kb.frying_kb) 
    #Пробелы нужны для ровного расположения пунктов в сообщении от бота.


@router.message(F.text == constants.GALLERY)
async def pickle_handler(msg: Message):
    await msg.answer('👍🏻 Здесь хранятся Ваши шедевры', reply_markup = kb.gallery_kb) 
    #Пробелы нужны для ровного расположения пунктов в сообщении от бота.


@router.message(F.text == "Меню")
async def menu(msg: Message):
    await msg.answer(constants.MENU, reply_markup = kb.menu_kb)


@router.message(F.text == 'Галерея')
async def galery_handler(msg: Message):
    await msg.answer(constants.GALLERY, reply_markup = kb.gallery_kb)