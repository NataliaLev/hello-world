# -*- coding: utf-8 -*-
import config
import telebot
import datetime, time
from threading import Thread

bot = telebot.TeleBot(config.token)
#bot = telebot.TeleBot("424475122:AAHZ8iO6KHSTmACSBVlpDH4YKHLwxuXPslc")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)