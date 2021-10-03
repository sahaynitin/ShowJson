import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""
