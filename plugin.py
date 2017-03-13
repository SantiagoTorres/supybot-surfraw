###
###

from supybot.commands import *
import supybot.plugins as plugins
import supybot.callbacks as callbacks
import supybot.schedule as schedule
import supybot.ircdb as ircdb
import supybot.ircmsgs as ircmsgs
import supybot.log as log
import supybot.conf as conf


import subprocess, shlex


class Surfraw(callbacks.Plugin):
    """
    First iteration of this shite
    """

    # These parameters are per-channel parameters
    self.browser = None

    def surfraw(self, irc, msg, args):
        """
        call surfraw with the appropriate arguments
        """

        if not self.browser:
            self.browser = self.registryValue('browser')


        currentChannel = msg.args[0]

        if irc.isChannel(currentChannel):
            thiscommand = "surfraw -browser={browser} {query}".format(
                    browser=self.browser, query=msg.args[1]);
            proc = subprocess.Popen(shlex.split(thiscommand),
                    stdout=subprocess.PIPE)

            try:
                stdout, stderr = proc.communicate()
                irc.reply(stdout)
            except OSError as e: 
                irc.error("shit has hit the fan, please check the log")
                raise


    surfraw = wrap(surfraw)

Class = Surfraw

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
