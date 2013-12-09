from org.freecode.irc.votebot.api import ExternalModule

import md5

class MD5Module(ExternalModule):
    def getName(self):
        return 'md5'

    def processMessage(self, privmsg):
	msg = privmsg.getMessage()[4:]
	m = md5.new(msg).digest()
	privmsg.send('MD5: ' + str(m))

    def getParameterRegex(self):
        return '.+'
