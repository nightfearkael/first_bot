import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = telebot.TeleBot('place_bot_token')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add('Да', 'Нет')
kb_remove = ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def start_message(message):
    first_message = bot.send_message(message.chat.id, 'Начнем диалог?', reply_markup=kb)
    bot.register_next_step_handler(first_message, second_message)


def second_message(message):
    first_text = message.text
    second_msg = bot.send_message(message.chat.id, f'Сделай второй выбор', reply_markup=kb)
    additional_param = 'Текстовая переменная'
    bot.register_next_step_handler(second_msg, third_message, first_text, additional_param)


def third_message(second_mess, start_text, new_param):
    bot.send_message(second_mess.chat.id, f'''Текст твоих сообщений:
Первое: {start_text}
Второе: {second_mess.text}
Дополнительная переменная из второй функции: {new_param}
''', reply_markup=kb_remove)


bot.polling()

