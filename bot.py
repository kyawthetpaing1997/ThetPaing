import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '8686636473:AAGUGWzpHJ1hKfzQ1h8azB86poonWAG9jNI'
bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

WEB_APP_URL = 'https://kyawthetpaing1997.github.io/ThetPaing/'
IMAGE_URL = 'https://imgur.com/a/IMrdKeo'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 Start Mine MRCT 🚀", web_app=web_app))
    
    welcome_text = "👋 Hello! Welcome to MRCT Official Bot 👋\n\nYou Can Start Mining MRCT Journeys.\n👇👇👇👇👇👇👇👇👇"
    
    bot.send_photo(
        message.chat.id,
        IMAGE_URL,
        caption=welcome_text,
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
