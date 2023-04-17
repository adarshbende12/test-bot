import telebot
bot = telebot.TeleBot('6138384898:AAEzKju6XSPYeyfojKJf5uuI9QdUwqo_9mE')
@bot.message_handler(commands=['start'])
def start(message):
    with open('images/bingo.jpeg','rb') as photo:
        bot.send_photo(message,photo=photo,caption="hii ra")
print("bot started")
bot.polling()
