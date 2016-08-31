#!/usr/bin/env python
# encoding: utf-8
"""
Example for testing weak referencing

Usage:
    python example05.py weak    # running signal testing with weak reference
                                # and you can only see one signal callback called
    python exapmle05.py strong  # running signal testing with strong reference
                                # and you can see two signal callback called

Notice:
    **connect** or **connect_via** with arg **weak** is True
        the Signal will hold a weakref to receiver and
        automatically disconnect when receiver goes out of scope or
        is garbage collected.
"""
import sys

from blinker import Signal


weak_signal = Signal('weak_signal')

def test_strong():
    @weak_signal.connect_via(Signal.ANY)
    def receive_data(sender, **kw):
        print ("Caught strong signal from : {}, data: {}".format(sender, kw))
        return "test"

def test_weak():
    @weak_signal.connect_via(Signal.ANY, weak=True)
    def receive_data(sender, **kw):
        print ("Caught weak signal from : {}, data: {}".format(sender, kw))
        return "test"

@weak_signal.connect_via(Signal.ANY, weak=True)
def receive_data2(sender, **kw):
    print ("Caught signal2 from : {}, data: {}".format(sender, kw))
    return "received2"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'strong':
            test_strong()
        else:
            test_weak()
    result = weak_signal.send('anonymous', abc=123)
    print(result)
