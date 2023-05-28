# -*- coding: utf-8 -*-
import os
import telebot
import logging
import sys


root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


DABOT_TOKEN_KEY = "DABOT_TOKEN"

token = os.getenv(DABOT_TOKEN_KEY)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    welcome_msg = f"Hello, {message.from_user.first_name} {message.from_user.last_name}"
    bot.send_message(message.chat.id, welcome_msg)

    logging.debug(f"welcome message sent to {message.from_user.first_name}")


@bot.message_handler()
def start_message(message):
    logging.debug(f"got incoming message: {message.text}")

    if message.text[-3:] == (' да' or ' Да' or ' ДА') or message.text == ('да' or 'Да' or 'ДА'):
        message_out = "ПИЗДА"
        bot.send_message(message.chat.id, message_out)
        logging.debug(f"sent chad message: {message_out}")
    else:
        pass


bot.polling(non_stop=True)
