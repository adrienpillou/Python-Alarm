# Author : Adrien Pillou
# Date : 02/11/2020

import time
import threading


# Alarm class
# Similar to GameMaker alarm block
class alarm(threading.Thread):

    # Alarm constructor (delay in ms)
    def __init__(self, delay, start_now=True):
        self.delay = delay
        self.start_time = time.time()
        self.ended = False
        self.remaining_time = delay
        if start_now:
            self.process()

    # Check if the alarm ended
    def is_ended(self):
        if self.start_time is None:
            return False
        return self.ended

    # Return the remaining time (ms)
    def get_remaining_time(self):
        if self.ended:
            return 0
        else:
            return int(self.start_time + self.delay - time.time()) * 1000

    # Waiting a given delay
    def process(self):
        # Creating a non-blocking timer using threading module
        threading_timer = threading.Timer(self.delay * .001, self.end)
        threading_timer.start()

    # End callback
    def end(self):
        self.ended = True
        self.delay = 0
        self.remaining_time = 0

    # Start the alarm
    def start(self):
        self.start_time = time.time()
        self.process()

    # Reset the alarm
    def reset(self, delay):
        self.delay = delay
        self.start_time = time.time()
        self.ended = False
