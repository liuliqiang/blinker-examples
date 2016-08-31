#!/usr/bin/env python
# encoding: utf-8
"""
Example for testing blinker signal is **synchronized**

Usage:
    python example03.py # you can get an exception and one line printout
                        # Caught signal from : anonymous, data: {'abc': 123}
                        # Traceback (most recent call last):
                        # File "example03.py", line 39, in <module>
                        # result = break_signal.send('anonymous', abc=123)
                        # File "/home/tyrael/.virtualenvs/test/lib/python3.5/site-packages/blinker/base.py", line 267, in send
                        # for receiver in self.receivers_for(sender)]
                        # File "/home/tyrael/.virtualenvs/test/lib/python3.5/site-packages/blinker/base.py", line 267, in <listcomp>
                        # for receiver in self.receivers_for(sender)]
                        # File "example03.py", line 29, in receive_data
                        # test = 1 / 0
                        # ZeroDivisionError: division by zero

Notice:
    Bliker signal is **synchronized**, by this example
    if some signal handler break, all handler would lose handler chance
    and whole application break
"""
from blinker import signal


break_signal = signal('break_signal')

@break_signal.connect
def receive_data(sender, **kw):
    print ("Caught signal from : {}, data: {}".format(sender, kw))
    test = 1 / 0
    return test

@break_signal.connect
def receive_data2(sender, **kw):
    print ("Caught signal2 from : {}, data: {}".format(sender, kw))
    return "received2"


if __name__ == "__main__":
    result = break_signal.send('anonymous', abc=123)
    print(result)
