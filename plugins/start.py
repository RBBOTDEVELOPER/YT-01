from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Youtube ❤", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Danuma_admin_bot")],
        [InlineKeyboardButton(
            "Bot channel 🧪",url="https://t.me/danumabots")]
    ])
    thumbnail_url = "https://telegra.ph/file/69a96df53932f1cd2174f.jpg"
    await message.reply_photo(thumbnail_url,caption="Hi **{message.from_user.first_name}**\nI'm glad to see you here\nWelcome to Speedest\nYouTube Downloader bot\n\n <b>Need to know howto use me ?</b>\n• Type /help to get instructins.\n • Type /tute for make a bot like me.\n • This bot is fully free.\n• Don't pay anyone for Bots like this. \n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
