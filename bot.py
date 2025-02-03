import telebot
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot('7593376134:AAExPwpZwz72p2oJP1BM1gadLzpC_rOo-qw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Давай начнем общение')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Здесь будет справочная информация')


@bot.message_handler(commands=['kartinka'])
def help_message(message):
    with open('blank_user.jpg', 'rb') as photo:
        bot.send_photo(chat_id=message.chat.id, photo=photo, caption='Моя картинка')


@bot.message_handler(commands=['kartinki'])
def help_message(message):
    file_list = ['blank_user1.jpg', 'blank_user2.jpg']
    input_files = [InputMediaPhoto(open('blank_user.jpg', 'rb'), caption='Групповое сообщение')]
    for file in file_list:
        input_files.append(InputMediaPhoto(open(file, 'rb')))
    bot.send_media_group(chat_id=message.chat.id, media=input_files)


@bot.message_handler(func=lambda message: 'привет' in message.text)
def choosen_message(message):
    bot.reply_to(message, 'Рад видеть тебя')


@bot.message_handler(func=lambda message: 'помощь' in message.text)
def choosen_message(message):
    bot.reply_to(message, 'Как я могу тебе помочь?')


@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.reply_to(message, 'Я обработал текстовое сообщение')


@bot.message_handler(content_types=['photo', 'document', 'video'])
def combined_message(message):
    bot.send_message(message.chat.id, 'Я получил сообщение с файлом')


bot.polling()

