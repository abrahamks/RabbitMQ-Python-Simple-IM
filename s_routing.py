#!/usr/bin/env python
import pika
import sys
import string
import random
#define variable
nickname = 'default'
#define connection
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         type='direct')
#define list of channels
list_of_channels = []
def nick_generator(size=6, chars=string.ascii_uppercase + string.digits):
	#source : http://stackoverflow.com/questions/2257441/python-random-string-generation-with-upper-case-letters-and-digits
	global nickname 
	nickname= ''.join(random.choice(chars) for x in range(size))
	return nickname

def set_nickname(nickname_input):
	global nickname
	nickname = nickname_input
	return nickname
	
def join_channel(chan_name):
	join_message = nickname + ' has just joined ' + chan_name
	channel.basic_publish(exchange='direct_logs',
                      routing_key=chan_name,
                      body=join_message)
	list_of_channels.append(chan_name)
	print 'your list of channels: ' + '[%s]' % ', '.join(map(str, list_of_channels))
	return "you've just joined Channel: "+ chan_name
	
def leave_channel(chan_name):
	leave_message = nickname + ' has just leaved ' + chan_name
	channel.basic_publish(exchange='direct_logs',
                      routing_key=chan_name,
                      body=leave_message)
	list_of_channels.remove(chan_name)
	print 'your list of channels: ' + '[%s]' % ', '.join(map(str, list_of_channels))
	return "you've just leaved Channel: "+ chan_name
	
def process_message(msg):
	#@<channelname><text>
	words = msg.split()
	if words[0][0] == '@':
		chan_name = words[0][1:]
		body_msg = nickname + '___' + ' '.join(words[1:])
		channel.basic_publish(exchange='direct_logs',
                      routing_key=chan_name,
                      body=body_msg)
		return nickname + ' >>> ' + body_msg
	else:
		#broadcast <msg> to all channels
		for list_item in list_of_channels:
			channel.basic_publish(exchange='direct_logs',
                      routing_key=list_item,
                      body=nickname + '___' + msg)
		return 'broadcast ' + msg + '[%s]' % ', '.join(map(str, list_of_channels))

def action_menu(cmd=''):
	if cmd =='':
		return 'please input your message'
	elif cmd !='':
		words = cmd.split()
		#command /NICK <nickname>
		if words[0] == '/NICK':
			if len(words)> 1:
				return 'your nickname: '+ set_nickname(words[1])
			else:
				return 'invalid argument'
		#command /JOIN <channelname>
		elif words[0] == '/JOIN':
			if len(words)> 1:
				if words[1] in list_of_channels:
					return "you're on channel " + words[1]
				else:
					return join_channel(words[1])
			else:
				return 'invalid argument'
		#command /LEAVE <channel>
		elif words[0] == '/LEAVE':
			if len(words)> 1:
				if words[1] in list_of_channels:
					return leave_channel(words[1])
				else:
					return "you're not on channel "+ words[1]
			else:
				return 'invalid argument'
		#command /EXIT
		elif words[0] == '/EXIT':
			connection.close()
			sys.exit(0)
			return 'bye2'
		#processing message
		else: 
			return process_message(cmd)
		
def main():
	print 'your nickname: '+ nick_generator()
	#words = user_cmd.split()
	#print words
	flag = True
	#create the menu
	while flag:
		user_cmd = raw_input('> ')
		print action_menu(user_cmd)
		
main()
connection.close()