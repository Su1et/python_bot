from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Токен бота (заміни на свій токен від BotFather)
TOKEN = os.getenv("TELEGRAM_TOKEN", "тут_твій_токен")

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Привіт {update.effective_user.first_name}!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Привіт {update.effective_user.first_name}!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Команда /start
    dp.add_handler(CommandHandler("start", start))
    # Будь-яке повідомлення
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print("Бот запущений...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
