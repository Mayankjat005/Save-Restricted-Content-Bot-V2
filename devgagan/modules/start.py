from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("MainChannel", url="https://t.me/WarriorUnitsBots")],        
        [InlineKeyboardButton("Anime Channel", url="https://t.me/Warrior_Units")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/oo7jatji")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://telegra.ph/file/0c3c0a72ca2785c0cf910.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
