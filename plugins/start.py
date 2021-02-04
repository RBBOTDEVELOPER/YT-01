from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/D_bot_Ai")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Danuma_admin_bot")],
            [InlineKeyboardButton("Developer",url="Https://lasiya.ml")]
    ])
    welcomed = f"[Hey](https://telegra.ph/file/d16beb00ebe1c13df3de3.jpg)<b>{message.from_user.first_name}</b> I'am YouTube Downloader \n From Danuma Project \n Enter /help for instructions"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
