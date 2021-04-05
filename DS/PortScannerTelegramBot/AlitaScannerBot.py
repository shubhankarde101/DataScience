# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:49:39 2021

@author: SHUBHANKAR

Simple Telegram Bot to automate the process

"""
# Imports
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
import PortScannerUsingPython as portscanner
import configparser as cfg
import os
assert os.path.exists('C:/Users/SHUBHANKAR/Desktop/My_Home_Projects/DS_Git/DS/PortScannerTelegramBot')
parser = cfg.ConfigParser()

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Command Handlers. Usually take two arguments: bot and update.
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome! My name is Alita. I am your bot. Currently I am trained on the below commands: 1)/start, 2)/bop, 3)/portscan arguments(localhost,protocol,portlow, porthigh)")


def portscan(update, context):

    # send the link back
    li = portscanner.main1(context.args[0],context.args[1],int(context.args[2]),int(context.args[3]))
    for i in li:
         context.bot.send_message(chat_id=update.message.chat_id, text=i)
    li.clear()


def echoText(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    # Create updater and pass in Bot's auth key.

    parser.read('C:\\Users\\SHUBHANKAR\\Desktop\\My_Home_Projects\\DS_Git\\DS\\PortScannerTelegramBot\\config.cfg')
    token = parser.get('creds', 'token')

    updater = Updater(token=token, use_context=True)
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('portscan', portscan))
    dispatcher.add_handler(CommandHandler('bop', bop))
    dispatcher.add_handler(MessageHandler(Filters.text, echoText))

    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()

if __name__ == '__main__':
    main()