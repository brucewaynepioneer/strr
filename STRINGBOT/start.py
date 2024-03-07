from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# Removed the import statement for OWNER_ID since it is not being used
def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

async def start(bot: Client, msg: Message):
    video = "start.mp4"  # Replace "link_to_video.mp4" with the direct link of the .mp4 video
    await bot.send_video(
        chat_id=msg.chat.id,
        video=video,
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
