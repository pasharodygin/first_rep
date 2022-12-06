import telebot

bot = telebot.TeleBot('5735861936:AAHj33x3tkPtLAkNIgvpo-Hbuk1ZhAZ5qB8')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}!</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю((...", parse_mode='html')


bot.polling(none_stop=True, interval=0)
