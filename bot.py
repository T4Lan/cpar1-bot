import sys
import time
import telepot
import re
from pprint import pprint

protips = []
karma = []

def persistMessage(msg):
	 f = open('Data/protips', 'a+')
	 f.write(msg)
	 f.write("\n")
	 f.close()

def handle_plano(bot, msg, chat_id, match):
	bot.sendPhoto(chat_id, "http://argentina.campus-party.org/files/large/89cc483747597b3")

def handle_gatito(bot, msg, chat_id, match):
	bot.sendPhoto(chat_id, "http://thecatapi.com/api/images/get?type=gif")

def handle_comollego(bot, msg, chat_id, match):
	bot.sendLocation(chat_id, -34.5614827695827, -58.50762742329734)

def handle_protips(bot, msg, chat_id, match):
	response="*Protips CPAR*\n"
	i = 1
	for protip in protips:
		response += "*%s-* %s\n" % (i, protip)
		i +=  1
	bot.sendMessage(chat_id, response, "Markdown")

def handle_karma(bot, msg, chat_id, match):
	response = karma.count(re.sub("karma ","",command))
	bot.sendMessage(chat_id, response)

def handle_cleanProtip(bot, msg, chat_id, match):
	index = match.group(1)
	print ("Removing protip #" + index)
	if int(index) < len(protips):
		protips.pop(int(index)-1)

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

			dispatcher = {
				'^plano$': handle_plano,
				'^bar$': handle_gatito,
				'^comollego$': handle_comollego,
				'^protips$': handle_protips,
				'^karma$': handle_karma,
				'^cleanProtip ([0-9]+)': handle_cleanProtip
			}

			for regex, handler in dispatcher.items():
				match = re.match(regex, command)
				if match:
					handler(bot, msg, chat_id, match)  
			return          

		protipMatch = re.match("^.*#protip (.*)", msg['text'])
		if protipMatch:
			protip = protipMatch.group(1)
			print ("Protip: {}".format(protip))
			protips.append(protip)
			persistMessage(protip)
			return

		karmaMatch = re.match("(\w+)\+\+", msg['text'])
		if karmaMatch:
			element = re.sub("\+\+",'',karmaMatch.group(1))
			print ("Karma +1 a :".format(element))
			karma.append(element)
			persistMessage(protip)
			return
		
		
TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
