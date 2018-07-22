from qqbot import QQBotSlot as qqbotslot, RunBot
 
@qqbotslot
 
 
def onQQMessage(bot, contact, member, content):


	Brain={"hello":"你好，我是QQ机器人,叫我小冰就是^-^","[@ME]  ":"@小冰干嘛！","在":"我一直在呢，嘻嘻","你好":"你好!","你叫什么名字":"小冰，小冰的xaio，小冰的bing～","你是男的还是女的":"它是什么样的?"}

	print(content)
	
	if content in Brain:
		bot.SendTo(contact,Brain[content])


if __name__ == '__main__':
	RunBot()
