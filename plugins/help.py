from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("Youtube tutorial", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")],
		 ])
	
    HelpT = f"<b>♔English help</b>\n• Just Send your Youtube video url⛓ \n• And i will give Method list to select your choice😋\n\n<b>♔සිංහල උදව්</b>\n• කොපි කරගත් Youtube ලින්කුව එවන්න.\n• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය පමාණය හා මාදිලිය තෝරාදෙන්න.\n\n Also use our file renamer @Renamerv12bot"
    thumbnail_url = "https://telegra.ph/file/a0c714ea372017109ff4c.jpg"
	
	await message.reply_photo(thumbnail_url,HelpT, reply_markup=Lasiya2)
