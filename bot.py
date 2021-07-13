import telebot

bot = telebot.TeleBot('1822250556:AAHNj4B-2GM105BoQh-bbz-O9PkLbQcV-Qk')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[-1] == 'а':
        bot.send_message(message.from_user.id, 'Хуй на!')
    elif message.text[-3:] == 'нет':
        bot.send_message(message.from_user.id, 'Минет!')

bot.polling(none_stop=True)

