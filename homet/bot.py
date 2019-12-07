from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, time, datetime
import logging


PROXY={'proxy_url':'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs':{'username':'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log')
def greet_user(bot, update):

    text='Ну привет, Никита, как дела?'
    print(text)
    update.message.reply_text(text)

def time(bot, update):

    show_time='Время работать!!!'
    print(show_time)
    update.message.reply_text(show_time)
    update.message.reply_text(today)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    
  



def main_function():
    mybot=Updater('857312210:AAHGwKWxtPzrzT0f6IIyjLQlOuBWvlurnH4', request_kwargs=PROXY)
    
    dp=mybot.dispatcher
    
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    today=date.today()



main_function()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
