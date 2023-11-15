from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from constants import PICKLE_GUIDE


menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Меню')]], resize_keyboard=True)

gallery_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Галерея')]], resize_keyboard=True)

def create_keyboard():
    kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Кнопка 1")
    button2 = KeyboardButton("Кнопка 2")
    kb1.row(button1, button2)
    return kb1