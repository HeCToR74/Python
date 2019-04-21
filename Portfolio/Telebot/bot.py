# -*- coding: utf-8 -*-
import config
import telebot

token = '677520731:AAHxkLG-aPbEUicFKr6q10LO3zWKM0ciHOw'

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	if message.text == "Привіт":
		bot.send_message(message.from_user.id, "Привіт! Лідочка, я тебе кохаю!!!")
	elif message.text == "Бувай!":
		bot.send_message(message.from_user.id, ":(((, не йди")
	else:
	    bot.send_message(message.chat.id, "Лідочка, я тебе кохаю!!!")

if __name__ == '__main__':
     bot.polling(none_stop=True)
