from qqbot import QQBotSlot as qqbotslot, RunBot
 
@qqbotslot
 
 
def onQQMessage(bot, contact, member, content):

    print(content)
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '在':
        bot.SendTo(contact, '我一直在呢，嘻嘻')
    elif content == '[@ME]  ':
        bot.SendTo(contact,'@小冰干嘛！')
	
    elif content == '-stop':
 
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
 
if __name__ == '__main__':
    RunBot()
