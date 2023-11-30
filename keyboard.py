from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from constants import FRYING_GUIDE, PICKLE_GUIDE, GALLERY


menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = FRYING_GUIDE)],
    [KeyboardButton(text = PICKLE_GUIDE)],
    [KeyboardButton(text = GALLERY)],
    ], resize_keyboard=True)

gallery_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Галерея')]], resize_keyboard=True)
