from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["tute"]),
async def start(client, message):

    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("⚜️ Go ⚜️", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")],
    ])
    tuter = f"[To make a YouTube downloader pess ⚜️ Go ⚜️ button to go youtube orexpand Instant viwe to watch video directly. 🥳]()"
    await message.reply_text(tuter)
