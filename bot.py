import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, request

load_dotenv()
TOKEN = os.getenv("TOKEN")

CHANNEL_LINK = "https://t.me/Haunted_Dorm_Community"
GAME_URL = "https://beporoa2468.github.io/Haunted-dorm/"  # আপনার Mini App URL
PORT = int(os.environ.get("PORT", 5000))

# Flask app
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()


# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Play Game", web_app=WebAppInfo(url=GAME_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎮 Welcome!\n\nPlease join our channel first, then click **Play Game** to start.",
        reply_markup=reply_markup
    )


# Register command handler
application.add_handler(CommandHandler("start", start))


# --- Webhook route ---
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"


@app.route("/")
def home():
    return "Bot is running with Webhook!"


if __name__ == "__main__":
    # Set webhook URL (your Render domain)
    RENDER_URL = os.environ.get("https://telegram-bot-worker-xp8h.onrender.com")  # e.g. https://your-app.onrender.com
    if RENDER_URL:
        application.bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")

    app.run(host="0.0.0.0", port=PORT)
