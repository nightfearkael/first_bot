import telebot
from telebot.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

bot = telebot.TeleBot('place_bot_token')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text='Отправить контакт', request_contact=True))
kb_rm = ReplyKeyboardRemove()


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Пожалуйста, поделитесь своим контактом, чтобы менеджер мог с вами связаться', reply_markup=kb)


@bot.message_handler(content_types=['contact'])
def contact_message(message):
    bot.send_message(message.chat.id, 'Благодарю, в ближайшее время с вами свяжутся', reply_markup=kb_rm)
    managers_group_id = -123123123
    bot.forward_message(chat_id=managers_group_id, from_chat_id=message.chat.id, message_id=message.id)

bot.polling()
