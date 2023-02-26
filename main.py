"""
This module contains an implementation of the Bakery algorithm.

The Bakery algorithm assures mutual exclusion of N threads.
Beware! This is an example and may not actually work correctly ;)
"""

__author__ = "Tomáš Vavro", "Dominika Bemberáková"
__email__ = "xvavro@stuba.sk", "xbemberakova@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread
from time import sleep

DEFAULT_NUM_RUNS = 10
NUM_THREADS = 3


# array representing the interest of each process in the critical section
choose = [False] * NUM_THREADS
# array representing the order in which each process will receive access to the resource
number = [0] * NUM_THREADS


def bakery_algorithm(tid: int):
    global choose, number

    # assign order to process
    choose[tid] = True
    number[tid] = max(number) + 1
    choose[tid] = False

    # wait for other processes to release the critical section
    for j in range(NUM_THREADS):
        # skip current process
        if j == tid:
            continue
        # wait for processes currently deciding on entering the critical section
        while choose[j]:
            pass
        # wait until process with lower number has finished
        while (number[j] != 0) and ((number[j], j) < (number[tid], tid)):
            pass

    # critical section
    # print(f"Thread {tid} is entering the critical section.")
    sleep(1)
    print(f"Thread {tid} is leaving the critical section.")

    # release order of process
    number[tid] = 0


def process(tid: int, num_runs: int):
    """Simulates a process.

    Arguments:
        tid      -- thread id
        num_runs -- number of executions of the critical section
    """
    for _ in range(num_runs):
        bakery_algorithm(tid)


if __name__ == '__main__':
    threads = [Thread(process, i, DEFAULT_NUM_RUNS) for i in range(NUM_THREADS)]
    [t.join() for t in threads]
