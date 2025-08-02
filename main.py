from pyrogram import Client, filters
from pyrogram.types import Message
import config
from quiz import get_question
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


app = Client(
    "quiz_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN)
app.run()