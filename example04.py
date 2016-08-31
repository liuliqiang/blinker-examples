#!/usr/bin/env python
# encoding: utf-8
"""
Example for using anonymous signals

Usage:
    python example04.py # You can see two line printed
                        # Alternate processing...
                        # Altprocess: <Alternate c completed
"""
from blinker import Signal


class AltProcessor:
    on_ready = Signal()
    on_complete = Signal()

    def __init__(self, name):
        self.name = name

    def go(self):
        self.on_ready.send(self)
        print ("Alternate processing...")
        self.on_complete.send(self)

    def __repr__(self):
        return "<Alternate {}".format(self.name)

apc = AltProcessor('c')
@apc.on_complete.connect
def completed(sender):
    print ("Altprocess: {} completed".format(sender))

if __name__ == "__main__":
    apc.go()
