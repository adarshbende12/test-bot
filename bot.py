import telebot
bot = telebot.TeleBot('6138384898:AAEzKju6XSPYeyfojKJf5uuI9QdUwqo_9mE')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'hii {message.from_user.first_name}')
print("bot started")
bot.polling()