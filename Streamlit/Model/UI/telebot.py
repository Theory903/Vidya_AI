import logging
import os
import datetime
from dotenv import load_dotenv
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters

# Load environment variables
load_dotenv()
telegram_token ="6025474546:AAEwKFJO4Esi8ylju8saSdhktJ1t9WOe6uw"

# Define the folder to save chat history files
chat_history_folder = 'chat_history'

# Create the folder if it doesn't exist
if not os.path.exists(chat_history_folder):
    os.mkdir(chat_history_folder)

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Telegram Updater
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

def main(update: Update, context: CallbackContext) -> None:
    try:
        chat_text = update.message.text
        chat = ""
        chat += f"{update.message.from_user.username}: {chat_text}\n"
        prompt = f"{chat}\nSnapBot: "
        
        # Simulate your existing 'main' function
        response = simulate_main_function(prompt)

        # Send the response
        update.message.reply_text(response)

        # Create a separate .txt file for each chat history with date and time
        current_date = datetime.date.today()
        chat_file_name = f'{update.message.from_user.username}_{current_date}_chat_history.txt'
        chat_file_path = os.path.join(chat_history_folder, chat_file_name)
        with open(chat_file_path, 'a') as chat_file:
            chat_file.write(prompt)
            chat_file.write(response + '\n')
    except Exception as e:
        logger.error(e)

def simulate_main_function(prompt: str) -> str:
    # You can simulate your existing 'main' function here
    # Replace this with your actual logic
    response = f"This is a simulated response to: {prompt}"
    return response

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your SnapBot. Send me a message, and I'll respond!")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is SnapBot. Send me any message, and I'll respond as SnapBot!")

# Handlers for commands
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

# Handler for regular messages (non-command messages)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, main))

def main_telegram_bot() -> None:
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main_telegram_bot()
