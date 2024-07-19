from pyrogram import Client, filters

# Configuration - replace with your own values
api_id = "YOUR_API_ID" "24491383"
api_hash = "YOUR_API_HASH"  "78e18eba669cc519ffd7a3c89f9ed32a"
bot_token = "YOUR_BOT_TOKEN"   "7374373768:AAH0rgmygV-Xee3Nz2Yf_WyytUlgHBGR5O4"

# Initialize the bot
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a handler for photo and video messages
@app.on_message(filters.photo | filters.video)
def thanks(client, message):
    message.reply_text("Thanks!")

# Run the bot
app.run()
