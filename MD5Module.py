from org.freecode.irc.votebot.api import ExternalModule

import hashlib


class MD5Module(ExternalModule):
    def getName(self):
        return 'md5'

    def processMessage(self, privmsg):
        msg = privmsg.getMessage()[5:]
        m = hashlib.md5()
        m.update(msg.encode('utf-8'))
        print msg
        privmsg.send('MD5: ' + m.hexdigest())

    def getParameterRegex(self):
        return '.+'


