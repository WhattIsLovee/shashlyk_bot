from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Dispatcher

import keyboard as kb

import constants

from database_engine import session

from models.article import Article


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
    await msg.answer('•🫙 Маринады – подобранные ботом рецепты\n•📒 Мои рецепты – записать свои рецепты\n•⭐️ Избранное – Ваши любимые рецепты от бота', reply_markup = kb.pickle_kb) 
    #Пробелы нужны для ровного расположения пунктов в сообщении от бота.


@router.message(F.text == constants.FRYING_GUIDE)
async def frying_handler(msg: Message):
    await msg.answer('•🪵 Гайды по жарке – подобранные ботом руководства\n•📒 Мои гайды – записать свои гайды\n•⭐️ Избранное – Ваши любимые гайды от бота', 
                     reply_markup = kb.frying_kb) 
    #Пробелы нужны для ровного расположения пунктов в сообщении от бота.


@router.message(F.text == constants.GALLERY)
async def gallery_handler(msg: Message):
    await msg.answer('👍🏻 Здесь хранятся Ваши шедевры', reply_markup = kb.gallery_kb) 


@router.message(F.text == '🪵 Гайды по жарке')
async def frying_guides_handler(msg: Message):
    articles = session.query(Article).filter(Article.type == 'frying').all()
    articles_list_html = ''
    for i, article in enumerate(articles):
        articles_list_html += f'{i + 1}. <a href="{article.link}">{article.title}</a>\n'
    await msg.answer(articles_list_html, reply_markup = kb.frying_kb, disable_web_page_preview = True)
