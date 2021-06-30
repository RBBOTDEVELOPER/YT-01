from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Youtube ❤", url="https://youtube.com/channel/UCvyQ9siIwXk0iGxxmmsNcZQ")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/HACKING_GANG_299")],
        [InlineKeyboardButton(
            "Bot channel 🧪",url="https://t.me/RoyalBotFamily")]
    ])
    thumbnail_url = "https://telegra.ph/file/69a96df53932f1cd2174f.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hi<b>{message.from_user.first_name}</b>\n\n<b>Instructions for use..</b>\n• Type /help to get instructins.\n• Type /tute for make a bot like me.\n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
