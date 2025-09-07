import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Завантажуємо змінні середовища з .env
load_dotenv()

# Беремо токен
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN не знайдено у .env!")

# Обробник команди /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"Привіт {user.first_name}!")

# Обробник будь-якого текстового повідомлення
def echo(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"Привіт {user.first_name}!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print("Бот запущено...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
