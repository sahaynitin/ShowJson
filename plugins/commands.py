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
