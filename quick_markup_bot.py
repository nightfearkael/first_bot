import telebot
from telebot.util import quick_markup


bot = telebot.TeleBot('place_bot_token')

emoji_german = u"\U0001F1E9" + u"\U0001F1EA"
emoji_ru = u"\U0001F1F7" + u"\U0001F1FA"


kb_servers = quick_markup({
    f'Server 1 {emoji_ru}': {'callback_data': 'server_1'},
    f'Server 2 {emoji_german}': {'callback_data': 'server_2'},
    f'Server 3 {emoji_ru}': {'callback_data': 'server_3'},
    f'Server 4 {emoji_german}': {'callback_data': 'server_4'},
    f'Server 5 {emoji_ru}': {'callback_data': 'server_5'},
    f'Server 6 {emoji_german}': {'callback_data': 'server_6'}
    })

kb_server1 = quick_markup({
    'Load average': {'callback_data': 'la_srv1'},
    'Memory usage': {'callback_data': 'mem_srv1'},
    'Назад': {'callback_data': 'назад'}
})
kb_server2 = quick_markup({
    'Load average': {'callback_data': 'la_srv2'},
    'Memory usage': {'callback_data': 'mem_srv2'},
    'Назад': {'callback_data': 'назад'}
})
kb_server3 = quick_markup({
    'Load average': {'callback_data': 'la_srv3'},
    'Memory usage': {'callback_data': 'mem_srv3'},
    'Назад': {'callback_data': 'назад'}
})
kb_server4 = quick_markup({
    'Load average': {'callback_data': 'la_srv4'},
    'Memory usage': {'callback_data': 'mem_srv4'},
    'Назад': {'callback_data': 'назад'}
})
kb_server5 = quick_markup({
    'Load average': {'callback_data': 'la_srv5'},
    'Memory usage': {'callback_data': 'mem_srv5'},
    'Назад': {'callback_data': 'назад'}
})
kb_server6 = quick_markup({
    'Load average': {'callback_data': 'la_srv6'},
    'Memory usage': {'callback_data': 'mem_srv6'},
    'Назад': {'callback_data': 'назад'}
})


callback_dict = {
    'la_srv1': 'url_for_la_1',
    'mem_srv1': 'url_for_mem_1',
    'la_srv2': 'url_for_la_2',
    'mem_srv2': 'url_for_mem_2',
    'la_srv3': 'url_for_la_3',
    'mem_srv3': 'url_for_mem_3',
    'la_srv4': 'url_for_la_4',
    'mem_srv4': 'url_for_mem_4',
    'la_srv5': 'url_for_la_5',
    'mem_srv5': 'url_for_mem_5',
    'la_srv6': 'url_for_la_6',
    'mem_srv6': 'url_for_mem_6',
}


@bot.message_handler(commands=['server'])
def server_message(message):
    bot.send_message(message.chat.id, 'Выбери сервер:', reply_markup=kb_servers)


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    data = call.data
    match data:
        case 'server_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server1)
        case 'server_2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server2)
        case 'server_3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server3)
        case 'server_4':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server4)
        case 'server_5':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server5)
        case 'server_6':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери график", reply_markup=kb_server6)
        case 'назад':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери сервер", reply_markup=kb_servers)
        case _:
            bot.send_message(chat_id=call.message.chat.id, text=callback_dict.get(data))
            bot.answer_callback_query(callback_query_id=call.id, text='График загружен')


bot.polling()
