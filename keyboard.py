from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from constants import FRYING_GUIDE, PICKLE_GUIDE, GALLERY, MENU, BACK, FAVORITES


menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = PICKLE_GUIDE)],
    [KeyboardButton(text = FRYING_GUIDE)],
    [KeyboardButton(text = GALLERY)],
    ], resize_keyboard=True)


frying_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '🪵 Гайды по жарке'), KeyboardButton(text = '📒 Мои гайды')],
    [KeyboardButton(text = FAVORITES), KeyboardButton(text = MENU)],
    ], resize_keyboard=True)


pickle_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '🫙 Маринады'), KeyboardButton(text = '📒 Мои рецепты')],
    [KeyboardButton(text = FAVORITES), KeyboardButton(text = MENU)],
    ], resize_keyboard=True)

gallery_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '＋ Добавить фото'), KeyboardButton(text = '❌ Удалить фото')],
    [KeyboardButton(text = '🖼️ Мои фото'), KeyboardButton(text = MENU)],
    ], resize_keyboard=True)
