#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Owner : <a href='https://telegram.dog/About_kailas'>Kailas_vg </a>\n○ Language : <code>Java</code>\n○ Library : <a href='https://t.me/PK_Links/21'>Pranav Movies </a>\n○ Source Code : <a href='https://t.me/about_kailas/36 </a>\n○ Channel : @Kerala_villas\n○ Support Group : @Kerala_villa</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
