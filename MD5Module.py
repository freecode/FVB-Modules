from org.freecode.irc.votebot.api import ExternalModule

import hashlib

class MD5Module(ExternalModule):
    def getName(self):
        return 'md5'

    def processMessage(self, privmsg):
	msg = privmsg.getMessage()[4:]
	m = hashlib.md5()	
	digest  = md5.new(msg.encode('utf-8')).digest()
	privmsg.send('MD5: ' + digest.hexdigest())

    def getParameterRegex(self):
        return '.+'
