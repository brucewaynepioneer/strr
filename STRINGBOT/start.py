from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.private & filters.command("start"))
async def start(bot: Client, msg: Message):
    gif = "start.mp4"  # Replace "link_to_video.mp4" with the direct link of the .mp4 video
    await bot.send_animation(
        chat_id=msg.chat.id,
        animation=gif,
        caption=f"""Welcome to String Bot!

This is an advanced Pyrogram and Telethon string session generator bot made with ❤️ by [Team SPY](https://t.me/dev_gagan).

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Generate String", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("Support", url="https://devgagan.in/"),
                    InlineKeyboardButton("Official", url="https://t.me/stringsessionAK47")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
