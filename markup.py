from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn6 = KeyboardButton('🔙Назад')

# --- Main Menu ---
btn1 = KeyboardButton('🎯 Тренировки')
btn2 = KeyboardButton('✅Консультации')
btn3 = KeyboardButton('🚀 Обо мне')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2, btn3)

# --- Other Menu ---
btn4 = KeyboardButton('🏅Персональная тренировка')
btn5 = KeyboardButton('🖥Онлайн-ведение')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn4, btn5, btn6)

# --- Other Menu ---
btn7 = KeyboardButton('🏋️Программа тренировок')
otherMeny = ReplyKeyboardMarkup(resize_keyboard = True).add(btn7, btn6)
