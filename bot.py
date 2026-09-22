import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '8686636473:AAGUGwzpHJ1hKfzQ1h8azB86poonWAG9jnI'
bot = telebot.TeleBot(TOKEN)

try:
    bot.delete_webhook(drop_pending_updates=True)
except:
    pass

WEB_APP_URL = 'https://kyawthetpaing1997.github.io/ThetPaing/'
IMAGE_URL = 'https://i.imgur.com/a/IWrdKeo'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    # အမှန်ပြင်ဆင်ထားသော Web App ခလုတ်ချိတ်ဆက်ပုံ
    markup.add(InlineKeyboardButton("🚀 Start Mine MRCT 🚀", web_app=WebAppInfo(url=WEB_APP_URL)))
    
    welcome_text = "👋 Hello! Welcome to MRCT Official Bot 👋\n\nYou Can Start Mining MRCT Journeys. 👇👇👇👇👇👇"
    
    bot.send_photo(
        message.chat.id,
        IMAGE_URL,
        caption=welcome_text,
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
