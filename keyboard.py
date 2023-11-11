from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from constants import PICKLE_GUIDE


menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Меню')]], resize_keyboard=True)

gallery_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Галерея')]], resize_keyboard=True)