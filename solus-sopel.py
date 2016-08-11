#This code was written by krc4267 and is in the public domain. I don't care about it. It took me 2 hours. 
#This is a module for Sopel which was written for Solus' IRC channels.

from sopel import module

donate_msg = "If you'd like to support our efforts with Solus, we would love for you to donate! For a one-time donation, visit https://solus-project.com/support. If you would like to contribute monthly and get perks, head on over to our Patreon: https://patreon.com/solus."
bugs_msg = "You may report your bugs at bugs.solus-project.com."
cheatsheet0 = "Here are available shortcuts. If a shortcut has [nick] you can use it with a nickname, and the output will be prefixed by that nick."
cheatsheet1 = ".donate [nick]: Shows Solus donation links to the chat."
cheatsheet2 = ".bugs [nick]: Shows a link to the bugtracker. \n"
cheatsheet3 = ".packaging [nick]: Shows links to packaging guides. \n"
cheatsheet4 = ".chat [nick]: Sends people to solus-chat. \n"
cheatsheet5 = ".livestream [nick]: Sends people to solus-livestream. \n"
cheatsheet6 = ".cheatsheet: ...um"
packaging_msg = "There is a text packaging gude here: https://wiki.solus-project.com/Packaging, As well as a video packaging guide by Josh here: https://www.youtube.com/watch?v=kIaY1Bro3ag"
chat_msg = "Please use #Solus-Chat for offtopic. #Solus is for support only."
livestream_msg = "Livestream chatter is in #Solus-Livestream!"

@module.commands('donate','bugs','packaging','packaging-video','cheatsheet','chat','livestream') #Define commands which are programmed here so sopel knows what to do
def commands(bot, trigger):
	if trigger.group(1) == 'donate': #The donate message
		if trigger.group(2) == None: #Checks if you specified a nick
			bot.say(donate_msg) #Sends just the message
		else:
			bot.say(trigger.group(2)+': '+donate_msg) #If you specified a nick, adds it, and sends the message
	
	if trigger.group(1) == 'bugs': #The bugtracker message
		if trigger.group(2) == None: #Refer to comments on donate
			bot.say(bugs_msg)
		else:
			bot.say(trigger.group(2)+': '+bugs_msg)
			
	if trigger.group(1) == 'packaging': #The packaging message
		if trigger.group(2) == None: #Refer to comments on donate
			bot.say(packaging_msg)
		else:
			bot.say(trigger.group(2)+': '+packaging_msg)
			
	if trigger.group(1) == 'cheatsheet': #Sends you a commands cheat sheet
		bot.reply("I'm sending you all the shortcuts in a private message!") #Tells you what it's doing
		bot.say(cheatsheet0, trigger.nick) #PMs you the cheat sheet
        bot.say(cheatsheet1, trigger.nick)
        bot.say(cheatsheet2, trigger.nick)
        bot.say(cheatsheet3, trigger.nick)
        bot.say(cheatsheet4, trigger.nick)
        bot.say(cheatsheet5, trigger.nick)
        bot.say(cheatsheet6, trigger.nick)
	if trigger.group(1) == 'chat': #The chat message
		if trigger.group(2) == None: #Refer to comments on donate
			bot.say(chat_msg)
		else:
			bot.say(trigger.group(2)+": "+chat_msg)
	if trigger.group(1) == 'livestream': #The livestream message
		if trigger.group(2) == None: #Refer to comments on donate
			bot.say(livestream_msg)
		else:
			bot.say(trigger.group(2)+": "+livestream_msg)
