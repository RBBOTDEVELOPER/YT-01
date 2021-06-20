from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Youtube ❤", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")],
        [InlineKeyboardButton("Report Bugs 😊", url="https://t.me/Danuma_admin_bot")],
        [InlineKeyboardButton("Bot channel 🧪",url="https://t.me/danumabots")],
        [InlineKeyboardButton("",url="https://t.me/danumabots")]
    ])
    welcomed = f"Hi <b>{message.from_user.first_name}</b>\nI'm glad to see you here\nWelcome to Speedest\nYouTube Downloader bot\n\n <b>Need to know howto use me ?</b>\n• Type /help to get instructins.\n • Type /tutorial for make a bot.\n • This bot is fully free.\n• Don't pay anyone for Bots like this. \n───── ❝<b> Lets Play </b>❞ ─────\n "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
