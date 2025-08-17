import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

load_dotenv()
TOKEN = os.getenv("TOKEN")

CHANNEL_LINK = 'https://t.me/Haunted_Dorm_Community
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Play Game", callback_data='play_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome! Please join our channel and then click 'Play Game' to start.", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'play_game':
        query.edit_message_text(text="Game is starting...")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()