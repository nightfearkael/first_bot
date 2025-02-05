import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('place_bot_token')

inline_kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Подписаться на канал', url='https://dzen.ru/sys_notes')
inline_kb.add(button)

reg_keyboard = InlineKeyboardMarkup()
reg_keyboard.add(InlineKeyboardButton(text='Подписаться', callback_data='register_yes'),
                 InlineKeyboardButton(text='Отказаться', callback_data='register_no',))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Подпишись на канал, здесь много всего интересного', reply_markup=inline_kb)


@bot.message_handler(commands=['reg'])
def reg_message(message):
    bot.send_message(message.chat.id, 'Хотите подписаться?', reply_markup=reg_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    match call.data:
        case 'register_yes':
            bot.send_message(call.message.chat.id, 'Registered')
            bot.answer_callback_query(callback_query_id=call.id, text='Successfully registered')
        case 'register_no':
            bot.send_message(call.message.chat.id, 'Not registered')
            bot.answer_callback_query(callback_query_id=call.id, text='Not registered')


bot.polling()
