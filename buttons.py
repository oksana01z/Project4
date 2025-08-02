from pyrogram.types import KeyboardButton, InlineKeyboardButton
from pyrogram import emoji

# Общие кнопки
back_button = KeyboardButton(f"{emoji.BACK_ARROW} Назад")

# Кнопки главного меню


cats_button = KeyboardButton(f"{emoji.CAT} Котики")



cats_random_inline_button = InlineKeyboardButton(f"{emoji.CAT} Котики", callback_data="random_cat")
film_inline_button = InlineKeyboardButton("🎥 Фильм из базы", callback_data="film_from_db")