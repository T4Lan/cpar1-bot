import sys
import time
import telepot
import re
from pprint import pprint

protips = []

def persistMessage(msg):
     f = open('Data/protips', 'a+')
     f.write(msg)
     f.write("\n")
     f.close()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg)
    if content_type == 'text':
        matchObj = re.match("^campusbot (.*)", msg['text'])
        if matchObj:
            command = matchObj.group(1)
            command.lower()
            fromUser = msg['from']['username']
            print("[Command] ", command, " from ", fromUser)
            if command == 'plano':
                bot.sendPhoto(chat_id, "http://argentina.campus-party.org/files/large/89cc483747597b3")
            if command == 'quien sos':
                bot.sendMessage(chat_id, "Soy el bot de la Campus Party Argentina y estoy para ayudarte!")
            if command == 'como llego':
                bot.sendLocation(chat_id, -34.5614827695827, -58.50762742329734)
            if command == 'protips':
                response = ""
                for protip in protips:
                    response+=protip
                    response+="\n"
                    bot.sendMessage(chat_id,response)

        else:
            protipMatch = re.match("^.*#protip(.*)", msg['text'])
            if protipMatch:
                protip = protipMatch.group(1)
                print "Protip: {}".format(protip)
                protips.append(protip)
                persistMessage(protip)

        if msg['text'] == 'whoareyou':
            bot.sendMessage(chat_id, "I'm a Bot programmed in Python, and y'all suck.")
        if msg['text'] == 'guia':
            bot.sendPhoto(chat_id, "http://argentina.campus-party.org/files/large/006225d505808e6")
        
        
TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)