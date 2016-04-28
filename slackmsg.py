#!/usr/bin/env python2.7
"""
slackmsg handles sending messages via slack
"""

import sys
import getopt
from urllib import urlencode
import pycurl
import cStringIO


class SlackMsg(object):
    """
    SlackMsg handles sending messages via slack
    """

    def __init__(self, hook, channel="#random", user="slackbot", icon=":slack:"):
        self.channel = channel
        self.user = user
        self.icon = icon
        self.hook = hook

    def send(self, text):
        payload = '{"channel": "%s", "username": "%s", "icon_emoji": "%s", "text": "%s"}'\
                  % (self.channel, self.user, self.icon, text)
        postdata = urlencode({'payload': payload})
        curl = pycurl.Curl()
        curl.setopt(curl.POSTFIELDS, postdata)
        curl.setopt(curl.URL, self.hook)
        message = cStringIO.StringIO()
        curl.setopt(curl.WRITEFUNCTION, message.write)
        curl.perform()
        if curl.getinfo(pycurl.HTTP_CODE) != 200:
            raise ValueError('HTTP return code is not 200 OK: %s' % message.getvalue())


if __name__ == "__main__":
    opts, _ = getopt.getopt(sys.argv[1:], 'c:u:i:t:h:')

    for opt, arg in opts:
        if opt == '-c':
            flag_channel = arg
        elif opt == '-u':
            flag_user = arg
        elif opt == '-i':
            flag_icon = arg
        elif opt == '-t':
            flag_text = arg
        elif opt == '-h':
            flag_hook = arg
        else:
            assert False, "Unknown option: %s" % opt

    try:
        sm = SlackMsg(flag_hook)
    except NameError:
        exit(1)

    try:
        sm.channel = flag_channel
    except NameError:
        pass

    try:
        sm.user = flag_user
    except NameError:
        pass

    try:
        sm.icon = flag_icon
    except NameError:
        pass

    try:
        sm.send(flag_text)
    except NameError:
        exit(1)
    except ValueError as e:
        print str(e)
        exit(2)
    except Exception:
        exit(2)
