from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	
    helptxt = f"• Just Send Youtube Url \n • And i will give Method list  \n Youcan use  @Renamerv12bot & @Dprojbot"
    await message.reply_text(helptxt)
