import sys
import time
import telepot
import re
from pprint import pprint
import markovify

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg)

    if content_type == 'text':
        if msg['text'] == 'quiensos':
            bot.sendMessage(chat_id, "Soy el bot de la Campus Party Argentina y estoy para ayudarte!")
        if msg['text'] == 'plano':
            bot.sendPhoto(chat_id, "http://argentina.campus-party.org/files/large/89cc483747597b3")
        if msg['text'] == 'guia':
            bot.sendPhoto(chat_id, "http://argentina.campus-party.org/files/large/006225d505808e6")
        
        
TOKEN = '299391109:AAGOfxhynll7-bwBZfvLeZRVFnxg4mfOR-Q'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)