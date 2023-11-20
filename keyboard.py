from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Меню')]], resize_keyboard=True)

gallery_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Галерея')]], resize_keyboard=True)

class MyKeyboard:
    @staticmethod
    def get_keyboard():
        button1 = KeyboardButton('Button 1')
        button2 = KeyboardButton('Button 2')
        
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(button1, button2)
        
        return keyboard