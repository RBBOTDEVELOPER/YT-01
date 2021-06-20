from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["tute"]))
async def start(client, message):
    await message.reply_text("To make a YouTube downloader pess ⚜️ Go ⚜️ button to go youtube orexpand Instant viwe to watch video directly. 🥳",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go ⚜️", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")]
        ]))
    
