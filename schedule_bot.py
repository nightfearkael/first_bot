import telebot
import schedule
import time
from threading import Thread

bot = telebot.TeleBot('place_bot_token_here')


def planned_job():
    users_ids = [123123123, 456456456, 789789789]
    for telegram_id in users_ids:
        with open('Report.xlsx', 'rb') as report:
            bot.send_document(chat_id=telegram_id, document=report, caption='Ежедневный отчет')


def start_schedule():
    schedule.every().monday.at("08:00").do(planned_job, )
    schedule.every().tuesday.at("08:00").do(planned_job, )
    schedule.every().wednesday.at("08:00").do(planned_job, )
    schedule.every().thursday.at("08:00").do(planned_job, )
    schedule.every().friday.at("08:00").do(planned_job, )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    Thread(target=start_schedule, args=()).start()
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
