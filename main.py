"""
Program represents different sequences of using mutex

University: STU Slovak Technical University in Bratislava
Faculty: FEI Faculty of Electrical Engineering and Information Technology
Year: 2023
"""


__authors__ = "Dominika Bemberáková, Marián Šebeňa"
__email__ = "xbemberakova@stuba.sk, mariansebena@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"
from fei.ppds import Mutex, Thread, Semaphore
from time import sleep
from random import randint

# Set global variables
C = 5  # Number of customers
N = 3  # Size of waiting room

class Shared(object):

    def __init__(self):
        """
        Initialize shared variables.

        Mutex variable is used to synchronize access to the waiting room counter.
        Semaphores are used to signal the barber and the customers.
        """

        # TODO : Initialize patterns we need and variables
        self.mutex = Mutex()
        self.waiting_room = 0
        # Initialize rendezvous variables
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)


def get_haircut(i):

    """
    Simulate time required for haircut.

    :param i: customer identifier
    """
    print(f"Customer {i} is getting a haircut")
    sleep(randint(3, 5))

def cut_hair():

    """
    Simulate time required for cutting hair.
    """
    print("Barber is cutting hair")
    sleep(randint(3, 5))
    print(f"Barber is done cutting hair")


def balk(i):
    """
    Simulate situation when waiting room is full.

    :param i: customer identifier
    """
    print(f"Customer {i} is leaving because the waiting room is full")
    sleep(randint(5, 8))


def growing_hair(i):
    """
    Simulate situation when customer wait after getting haircut.
    Hair is growing and customer is sleeping for some time.

    :param i: customer identifier
    """
    print(f"Customer {i}'s hair is growing")
    sleep(randint(8, 14))


def customer(i, shared):
    """
    Implement the behavior of a customer.

    :param i: customer identifier
    :param shared: shared variables
    """
    while True:

        shared.mutex.lock()
        if shared.waiting_room < N:

            shared.waiting_room += 1
            print(f"Customer {i} entered the waiting room")
            shared.mutex.unlock()

            # Signal the barber that a customer is waiting
            shared.customer.signal()
            # Wait for the barber to invite the customer for a haircut
            shared.barber.wait()
            get_haircut(i)
            # Signal that the customer is done getting a haircut
            shared.customer_done.signal()
            # Wait for the barber to finish his work
            shared.barber_done.wait()
            # Leave waiting room and decrement counter
            shared.mutex.lock()
            shared.waiting_room -= 1
            print(f"Customer {i} left the waiting room")
            shared.mutex.unlock()
            growing_hair(i)

        else:
            # If waiting room is full, customer leaves and balks
            shared.mutex.unlock()
            balk(i)
            sleep(randint(1, 10) / 10)


def barber(shared):
    """Represents a barber thread"""
    while True:
        # Wait for a customer to signal that they are waiting
        shared.customer.wait()
        # Invite the customer for a haircut
        shared.barber.signal()
        # Cut the customer's hair
        cut_hair()
        # Signal that the barber is done cutting hair
        shared.barber_done.signal()
        # Wait for the customer to finish getting a haircut
        shared.customer_done.wait()


def main():
    shared = Shared()
    customers = []

    for i in range(C):
        customers.append(Thread(customer, i, shared))
    hair_stylist = Thread(barber, shared)

    for t in customers + [hair_stylist]:
        t.join()

# TODO: Global variables C = 5 numOfCustomers N = 3 sizeOfWaitingRoom


if __name__ == "__main__":
    main()