# Bemberakova_97392_feippds -01
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3102/)
[![License](https://img.shields.io/npm/l/@tandil/diffparse?color=%23007ec6)](https://github.com/dominikabemberakova/Bemberakova_97392_feippds/blob/main/LICENSE)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-blue.svg)](https://conventionalcommits.org)

# About 

The program represents a solution to the classic "Barber Shop" problem using mutex and semaphores in Python. The problem is to simulate the behavior of customers and a barber in a barber shop. Customers arrive randomly and enter a waiting room that has a limited capacity. When the waiting room is full, the customers leave and come back later. When a barber is available, they invite a waiting customer into the barber chair and cut their hair. After the haircut, the customer leaves and another customer is invited. The program runs indefinitely until it is manually stopped.

# Assignment
Your task in the second assignment is to implement the Barbershop problem with/without overtaking. Overtaking is optional. For the implementation, use the fei.ppds library threads. The source code must be compatible with Python 3.10.

The source code must:

1. contain a module header with a description of the module, author name, and license
2. be well-documented: each function (or class and its methods) must contain a docstring in accordance with PEP 257
3. be commented to a reasonable extent. Comments should be placed only where necessary for context understanding.
comply with PEP 8.

Write the documentation in the README.md file in the 02 branch (not in the README.md file you have in the master/main branch). In the documentation, describe the problem you are solving, how your code should be run, etc. (i.e., all the information a person who accidentally discovers your source code on the Internet might need).

Commit your work regularly, and your commit messages must be in accordance with CC. The deadline for submission is Monday, March 5, 2023, until 11:59 pm. Your repository must contain the given task by this time. The scoring for the task is divided as follows: 2 points for implementation, 2 points for documentation (justification), and 1 point for outputs. Try to be concise but informative.

You can find a sample from which you can derive your work in the annual repository, which is in the materials. Also, check the presentation.

Example output:
Note that your output does not have to be the same, and therefore, you can give the description of the output as part of the documentation. Before the last commit, check that the waiting room is set to 3, and the number of customers is set to 5.


# Problem solution:
The Barber Shop Problem is a classic synchronization problem, which involves a barber who cuts the hair of his customers in a barber shop. The barber shop has a waiting room with N chairs, where customers can wait for their turn. When there are no customers in the waiting room, the barber takes a nap. When a customer arrives, they take a seat in the waiting room. If there are no available chairs, the customer leaves and tries again later. When the barber wakes up, he invites the next customer in the waiting room for a haircut. After the haircut, the customer leaves the shop, and the barber goes back to sleep if there are no more customers waiting.

The Barber Shop Problem with Preemption extends the original problem by allowing the barber to be interrupted during a haircut. This means that if a new customer arrives while the barber is cutting the hair of another customer, the barber stops cutting and starts serving the new customer. After the new customer is done, the barber returns to the previous customer and continues cutting their hair.

The main challenge of this problem is to coordinate the access to the waiting room and the barber's chair, so that the customers and the barber do not interfere with each other. This can be achieved by using semaphores and mutexes, which ensure mutual exclusion and synchronization between the threads.

The solution presented in this code implements the Barber Shop Problem with Preemption using a shared object that contains semaphores and mutexes for synchronization. The `customer, barber, and helper functions get_haircut, cut_hair, balk, growing_hair` are implemented as separate threads. The customer function represents the behavior of a customer, while the barber function represents the behavior of a barber. The helper functions simulate different scenarios that can occur during the execution of the program.

The implementation uses a Mutex to protect the access to the waiting room counter and ensure mutual exclusion between threads. The waiting room counter is incremented when a customer enters the waiting room and decremented when a customer leaves. The implementation also uses four Semaphores to synchronize the access to the barber's chair and ensure that the barber and the customers do not interfere with each other.

Overall, the solution presented in this code provides an efficient and correct implementation of the Barber Shop Problem with Preemption, demonstrating the use of semaphores and mutexes for synchronization and mutual exclusion between threads.

# How to Run
The code can be run using any Python interpreter that supports the `fei.ppds library`. To run the code, save it as a `.py` file and run it from the command line using python `<filename>.py`. The code will execute and print output to the console.

# Functions 
I used the algorithm that was shown to us in the exercise.

## Shared class

The `Shared class` is used to share data between the threads. It has the following attributes:

`mutex:` Mutex used to synchronize access to the waiting_room variable.
`waiting_room:` Number of customers currently waiting in the waiting room.
`customer:` Semaphore used to signal the barber that a customer is waiting.
`barber:` Semaphore used to signal the customer that the barber is ready to cut their hair.
`customer_done:` Semaphore used to signal the barber that the customer is done getting a haircut.
`barber_done:` Semaphore used to signal the customer that the barber is done cutting their hair.

```python
class Shared(object):
    def __init__(self):
        # Initialize mutex and waiting room counter
        self.mutex = Mutex()
        self.waiting_room = 0
        # Initialize rendezvous variables
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)
```

## get_haircut(i) function

The `get_haircut(i)` function simulates the time it takes for a customer to get a haircut. It prints a message indicating that a customer is getting a haircut and sleeps for a random amount of time between 3 and 5 seconds.

```python
def get_haircut(i):

    print(f"Customer {i} is getting a haircut")
    sleep(randint(3,5))
```

## cut_hair() function

The `cut_hair()` function simulates the time it takes for the barber to cut a customer's hair. It prints a message indicating that the barber is cutting hair, sleeps for a random amount of time between 3 and 5 seconds, and then prints a message indicating that the barber is done cutting hair.

```python
def cut_hair():

    print("Barber is cutting hair")
    sleep(randint(3,5))
    print(f"Barber is done cutting hair")
```

## balk(i) function

The `balk(i)` function simulates the situation where a customer arrives at the barbershop and finds the waiting room full. It prints a message indicating that the customer is leaving and sleeps for a random amount of time between 5 and 8 seconds.

```python
def balk(i):

    print(f"Customer {i} is leaving because the waiting room is full")
    sleep(randint(5, 8))
```

## growing_hair(i) function

The `growing_hair(i)` function simulates the time it takes for a customer's hair to grow after getting a haircut. It prints a message indicating that the customer's hair is growing and sleeps for a random amount of time between 8 and 14 seconds.

```python
def growing_hair(i):

    print(f"Customer {i}'s hair is growing")
    sleep(randint(8,14))
```

## customer(i, shared) function

The `customer(i, shared)` function is a thread representing a customer. It runs in a loop and performs the following steps:

1. Acquires the mutex to access the waiting_room variable.
2. If the waiting room is not full, the customer enters the waiting room and increments the waiting_room counter. It then releases the mutex.
3. Signals the customer semaphore to indicate to the barber that a customer is waiting.
4. Waits on the barber semaphore to be invited for a haircut.
5. Gets a haircut by calling the get_haircut(i) function.
6. Signals the customer_done semaphore to indicate to the barber that the customer is done getting a haircut.
7. Waits on the barber_done semaphore for the barber to finish their work.
8. Acquires the mutex to access the waiting_room

```python
def customer(i, shared):
    while True:
        # Access waiting room counter
        shared.mutex.lock()
        if shared.waiting_room < N:
            # If waiting room is not full, customer enters and increments counter
            shared.waiting_room += 1
            print(f"Customer {i} entered the waiting room")
            # Release waiting room counter
            shared.mutex.unlock()

            # Signal the barber that a customer is waiting
            shared.customer.signal()
            # Wait for the barber to invite the customer for a haircut
            shared.barber.wait()
            # Get a haircut
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
```

## barber(shared) function

This function represents the behavior of the barber. It waits for a customer to signal that they are waiting, invites them for a haircut, cuts their hair, and signals that they are done. The function then waits for the customer to signal that they are done before repeating the process.

```python
def barber(shared):
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
```

## Printouts:
These printouts are from the barber solution and show the sequence of events that occur in the simulation. The simulation simulates a barber shop where customers come in to get their hair cut and the barber cuts their hair. The waiting room has limited capacity and when it's full, new customers leave.
```
Customer 0 entered the waiting room
Customer 1 entered the waiting room
Customer 2 entered the waiting room
Customer 3 is leaving because the waiting room is full
Customer 4 is leaving because the waiting room is full
Barber is cutting hair
Customer 1 is getting a haircut
Barber is done cutting hair
Barber is cutting hair
Customer 1 left the waiting room
Customer 1's hair is growing
Customer 0 is getting a haircut
Barber is done cutting hair
Customer 0 left the waiting room
Customer 0's hair is growing
Barber is cutting hair
Customer 2 is getting a haircut
Customer 4 entered the waiting room
Customer 3 entered the waiting room
Barber is done cutting hair
Customer 2 left the waiting room
Customer 2's hair is growing
Barber is cutting hair
Customer 4 is getting a haircut
Barber is done cutting hair
Customer 1 entered the waiting room
Customer 0 is leaving because the waiting room is full
Customer 4 left the waiting room
Customer 4's hair is growing

```

These printouts give a clear picture of how the simulation is running and how the barber and customers are interacting with each other.
