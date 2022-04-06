from asyncore import dispatcher
from cgitb import text
import imp
from turtle import update
from setuptools import Command
from telegram import *
from telegram.ext import *

bot = Bot("5179239822:AAHvRTTdN_LvZK7pQJVAMfj4p3o0lzSNup4")
#print(bot.get_me())
updater=Updater("5179239822:AAHvRTTdN_LvZK7pQJVAMfj4p3o0lzSNup4", use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="i'm @learnwithmrwebdev. This is my first telegram bot.",
    )

start_value=CommandHandler('Motion_detection', test_function)
dispatcher.add_handler(start_value)

updater.start_polling()