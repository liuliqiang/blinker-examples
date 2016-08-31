#!/usr/bin/env python
# encoding: utf-8
"""
Example for connect signal by decorator @signal_name.connect and get result

Usage:
    python example02.py # you can get two result after several seconds
                        # Caught signal from : anonymous, data: {'abc': 123}
                        # Caught signal2 from : anonymous, data: {'abc': 123}
                        # [(<function receive_data at 0x7f9cd5875840>, 'received'), \
                        #  (<function receive_data2 at 0x7f9cd584e9d8>, 'received2')]

Notice:
    Bliker signal is **synchronized**, by this example,
    you can not get the result before time.sleep finish
    so you need to notice signal process should not be abort
        or the whole application would break down.
"""
import time

from blinker import signal


send_data = signal('send_data')

@send_data.connect
def receive_data(sender, **kw):
    print ("Caught signal from : {}, data: {}".format(sender, kw))
    time.sleep(5)
    return "received"

@send_data.connect
def receive_data2(sender, **kw):
    print ("Caught signal2 from : {}, data: {}".format(sender, kw))
    return "received2"


if __name__ == "__main__":
    result = send_data.send('anonymous', abc=123)
    print(result)
