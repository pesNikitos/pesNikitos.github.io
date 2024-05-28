import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Вставьте сюда ваш токен
TOKEN = '6636195127:AAH5z_VkhtmGXf6b-yrzOoaxK7xGGSDWB2Q'
WEB_APP_URL = 'https://pesnikitos.github.io/'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание встроенной клавиатуры
    markup = InlineKeyboardMarkup()
    
    # Создание кнопки с Web App
    web_app = WebAppInfo(url=WEB_APP_URL)
    btn = InlineKeyboardButton(text='Перейти к игре', web_app=web_app)
    markup.add(btn)
    
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку ниже, чтобы перейти к игре:', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
