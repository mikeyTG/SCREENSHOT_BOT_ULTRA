from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi BRO {m.from_user.mention}.\n\nI'm Screenshot Bot PRO😋. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MY DP😒", url="https://telegra.ph/file/a49001f8ed1caaa8ce2fd.jpg"
                    ),
                    InlineKeyboardButton("Project Channel", url="https://t.me/MRGBOTREPAIR"),
                ],
                [InlineKeyboardButton("My Father", url="https://t.me/@YOUTUBERYT54355")],
            ]
        ),
    )
