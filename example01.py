#!/usr/bin/env python
# encoding: utf-8
"""
Example for testing `global registry of named signals`
usage:
    python example01.py         # you can't see anything print
                                # because nothing need to print
    python example01.py ready   # you can see something pring
                                # beacause signal sended

notice:
    signal.send(args)    # the args will be send to binded function
"""
import sys

from blinker import signal


def subscriber(sender):
    print("Got a signal sent by: {}".format(sender))

ready = signal('ready')
ready.connect(subscriber)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'ready':
            ready.send('arg1')
