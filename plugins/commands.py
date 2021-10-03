from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can help you to do stuff on Pdfs as well as convert images to Pdf. Use /help command to see features.

JUST SEND A PDF (or an image) to get started.

By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/tellybots_4u")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Tellybots_4u")],
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
        switch_pm_text=f"Hey i sent the json in PM 😉",
        switch_pm_parameter="start",
    )

    # Help Message
    HELP = """
**Usage**

1) Just send a PDF to do stuff on it
2) Send images to convert to PDFs

**Functions**
1) Rotate PDF Pages
2) Merge PDFs
3) Encrypt PDFs
4) Decrypt PDFs
5) Convert Images to PDF
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot with Pdf tools by @Tellybots_4u

Source Code : [Click Here](https://t.me/tellybots_digital)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Tellybots_4u
    """

