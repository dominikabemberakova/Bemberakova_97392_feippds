"""
Copyright 2023 Dominika Bemberakova.
Licensed to MIT https://spdx.org/licenses/MIT.html
This module implements the dining savages problem and it's solution.
"""


from time import *
from random import randint
from fei.ppds import Thread, Semaphore, Mutex, Event, print


"""
SERVINGS, SAVAGES and COOKS are model parameters.
    SERVINGS: the number of stewed missionary servings
        that will fit in the pot.
    SAVAGES: the number of savages in the tribe.
    COOKS: the number of cooks in the tribe.
"""
SERVINGS = 8
SAVAGES = 3
COOKS = 5


class SimpleBarrier(object):
    """
    SimpleBarrier object. Event is used to implement the turnstile.
    Args:
        threads_num(int): number of threads
    """

    def __init__(self, threads_num):
        """
        Initialize SimpleBarrier.
        Args:
            threads_num(int): number of threads
        """
        self.threads_num = threads_num
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        """
        The wait() function shall synchronize participating threads
        at the barrier until all threads have reached wait() specifying
        the barrier. After that all threads are released to continue.
        Args:
            each(str): string to be printed by each thread
            last(str): string to be printed by the last thread
        Returns:
            bool: returns true if the thread was last, false otherwise
        """
        self.mutex.lock()
        if each:
            print(each)
        self.count += 1
        is_last = False
        if self.count == self.threads_num:
            if last:
                print(last)
            self.count = 0
            is_last = True
            self.barrier.signal(self.threads_num)
        self.mutex.unlock()
        self.barrier.wait()
        return is_last