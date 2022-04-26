import telebot

bot = telebot.TeleBot('5379988612:AAF-7DWcf5e3I8LQEzRK9fJKaP-7uSGWHIk')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
    print(message)
if __name__ == '__main__':
    bot.infinity_polling()
