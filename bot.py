import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler
from flask import Flask
import threading

load_dotenv()
TOKEN = os.getenv("TOKEN")

CHANNEL_LINK = "https://t.me/Haunted_Dorm_Community"
GAME_URL = "https://beporoa2468.github.io/Haunted-dorm/"  # আপনার Mini App URL

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Play Game", web_app=WebAppInfo(url=GAME_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🎮 Welcome!\n\nPlease join our channel first, then click **Play Game** to start.",
        reply_markup=reply_markup
    )

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

# Flask app for Render health check
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    # Run bot in background thread
    threading.Thread(target=run_bot).start()

    # Run Flask server for Render health check
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
