import telebot
bot = telebot.TeleBot("6290167741:AAGklov1dXYAFGO6L8Y4yYW3ZfK5Mnv9fIU")


@bot.message_handler(commands=['start'])
def start_message(message):
  name_man = f"Hello, {message.from_user.first_name} {message.from_user.last_name}"
  bot.send_message(message.chat.id,name_man)

@bot.message_handler()
def start_message(message):
  if message.text[-3:] == (' да' or ' Да' or ' ДА') or message.text == ('да' or 'Да' or 'ДА'):
      bot.send_message(message.chat.id, "ПИЗДА")
  else:
    pass


bot.polling(non_stop=True)