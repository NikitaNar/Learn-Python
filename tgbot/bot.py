from telegram.ext import Updater, CommandHandler

PROXY={'proxy_url':'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs':{'username':'learn', 'password': 'python'}}

def greet_user(bot, update):
    text='Ну привет, Никита, как дела?'
    print(text)
    update.message.reply_text(text)

def time(bot, update):
    show_time='Время работать!!!'
    print(show_time)
    update.message.reply_text(show_time)




def main_function():
    mybot=Updater('857312210:AAHGwKWxtPzrzT0f6IIyjLQlOuBWvlurnH4', request_kwargs=PROXY)
    
    dp=mybot.dispatcher
    
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('time', time))

    mybot.start_polling()
    mybot.idle()



main_function()


