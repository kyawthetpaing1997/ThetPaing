import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# BotFather ဆီက ရထားတဲ့ သင့်ရဲ့ Token ကို ဒီနေရာမှာ ထည့်ပါ
TOKEN = '8686636473:AAGUGWzpHJ1hKfzQ1h8azB86poonWAG9jNI'


bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
# Web App လင့်ခ်နဲ့ ပုံလင့်ခ်ကို ဒီနေရာမှာ ထည့်ပါ။ 
WEB_APP_URL = 'https://wondrous-crostata-02d61c.netlify.app/'
IMAGE_URL = 'https://imgur.com/a/IMrdKeo'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # ဖန်တီးမယ့် Web App ခလုတ်
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEB_APP_URL)
    ​markup.add(InlineKeyboardButton("🚀 Start Mine MRCT 🚀", web_app=web_app))
    


    
  # ကြိုဆိုစာနှင့် ပုံကို ပပို့ပေးခြင်း    welcome_text = "မင်္ဂလာပါရှင်! MRCT Bot မှ ကြိုဆိုပါတယ်။ အောက်ပါခလုတ်ကို နှိပ်ပြီး Web App ကို ဝင်ရောက်နိုင်ပါတယ်။"
    bot.send_photo(
        message.chat.id, 
        IMAGE_URL, 
        caption=welcome_text, 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
