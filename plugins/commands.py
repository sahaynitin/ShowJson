import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},

💡 ** I am Telegram Json Extractor bot and Chatbase channel id generator bot **

`Send any Msg by own or Forward msg from your channel to get json details,you can also use IDs as Chatbase Token`

**👲 Maintained By: @Tellybots_4u**
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('Developer👨‍✈️', url=f"https://t.me/tellybots_4u")
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Client.on_message(filters.private & filters.incoming)
async def show_json(c, m):
    text = f'`{m}`'
    if len(text) <= 4096:
        await m.reply_text(text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await m.reply_document(f'Your json file {m.from_user.first_name}.json', True)
        os.remove(f'Your json file {m.from_user.first_name}.json')

@Client.on_inline_query()
async def inline_json(c, m):
    text = f'`{m}`'
    if len(text) <= 4096:
        await c.send_message(chat_id=m.from_user.id, text=text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await c.send_document(chat_id=m.from_user.id, file_name=f'Your json file {m.from_user.first_name}.json')
        os.remove(f'Your json file {m.from_user.first_name}.json')

    await m.answer(
        results=[],
        switch_pm_text=f"Hey i sent the json in PM ",
        switch_pm_parameter="start",
    )
