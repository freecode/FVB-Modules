from org.freecode.irc.votebot.api import ExternalModule

class ReplaceModule(ExternalModule):
    def getCommandCharacter(self):
        return ".+"

    def getName(self):
        return ".+"

    def getParameterRegex(self):
        return '.*'

    def processMessage(self, privmsg):
        privmsg.send(privmsg.getMessage()[5:])
