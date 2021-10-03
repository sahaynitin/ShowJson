import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""Hello {0}

I am a converter clone of [Convert Ns Bot](https://telegram.dog/convert_Ns_bot) by {1}

I can convert file to video or video to file with custom thumbnail support.
"""


#This will be appeared when anyone use help command

      HELP = """**Hey you need help 🤔 ?**

1. Send me the telegram file or video which you wanted to convert.

2. Send me the thumbnail(photo) optional.

3. Reply to video /converttofile for converting into file.

4. Reply to file /converttovideo for converting into video.

SUPPORT GROUP: [NS Bot Supporters](https://telegram.dog/Ns_Bot_supporters)
"""


#Please don't change this about command 🙏

      ABOUT = """
📝 Language: Python 3

🧰 Framework: Pyrogram

👨‍💻 Developer: [Anonymous](https://t.me/Ns_AnoNymouS)

📮 Channel: [NS BOT UPDATES](https://t.me/Ns_bot_updates)

👥 Group: [NS BOT SUPPOTERS](https://t.me/Ns_Bot_supporters)

💻 Source Code:[Press Me](https://github.com/Ns-AnoNymouS/TG-CONVERT-BOT)

"""

####################################################################################################################################################
####################################################################################################################################################


@Client.on_message(filters.private & filters.incoming)
async def show_json(c, m):
    text = f'{m}'
    if len(text) <= 4096:
        await m.reply_text(text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await m.reply_document(f'Your json file {m.from_user.first_name}.json', True)
        os.remove(f'Your json file {m.from_user.first_name}.json')

@Client.on_inline_query()
async def inline_json(c, m):
    text = f'{m}'
    if len(text) <= 4096:
        await c.send_message(chat_id=m.from_user.id, text=text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await c.send_document(chat_id=m.from_user.id, file_name=f'Your json file {m.from_user.first_name}.json')
        os.remove(f'Your json file {m.from_user.first_name}.json')

    await m.answer(
        results=[],
        switch_pm_text=f"Hey i sent the json in PM 😉",
        switch_pm_parameter="start",
    )
