from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
from config import TG_BOT_TOKEN, API_HASH, APP_ID, OWNER_ID

# Initialize the bot
bot = Client("settings_bot", api_id=APP_ID, api_hash=API_HASH, bot_token=TG_BOT_TOKEN)

# Define the settings panel
@bot.on_message(filters.command("settings") & filters.user(OWNER_ID))
async def open_settings(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Set API Key", callback_data="set_api_key")],
        [InlineKeyboardButton("Set Channel ID", callback_data="set_channel_id")],
        [InlineKeyboardButton("Set Force Sub Channel", callback_data="set_force_sub_channel")]
    ])
    await message.reply("Choose the setting to change:", reply_markup=keyboard)

# Handle callback queries
@bot.on_callback_query()
async def handle_callback_query(client, query: CallbackQuery):
    data = query.data

    if data == "set_api_key":
        await query.message.reply("Send me the new API key.")
        bot.set_parse_mode("default")
        await bot.listen(OWNER_ID)

    elif data == "set_channel_id":
        await query.message.reply("Send me the new Channel ID.")
        bot.set_parse_mode("default")
        await bot.listen(OWNER_ID)

    elif data == "set_force_sub_channel":
        await query.message.reply("Send me the new Force Sub Channel ID.")
        bot.set_parse_mode("default")
        await bot.listen(OWNER_ID)

# Start the bot
bot.run()
