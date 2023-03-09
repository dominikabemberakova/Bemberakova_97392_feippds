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

The solution presented in this code implements the Barber Shop Problem with Preemption using a shared object that contains semaphores and mutexes for synchronization. The **_customer, barber, and helper functions get_haircut, cut_hair, balk, growing_hair_** are implemented as separate threads. The customer function represents the behavior of a customer, while the barber function represents the behavior of a barber. The helper functions simulate different scenarios that can occur during the execution of the program.

The implementation uses a Mutex to protect the access to the waiting room counter and ensure mutual exclusion between threads. The waiting room counter is incremented when a customer enters the waiting room and decremented when a customer leaves. The implementation also uses four Semaphores to synchronize the access to the barber's chair and ensure that the barber and the customers do not interfere with each other.

Overall, the solution presented in this code provides an efficient and correct implementation of the Barber Shop Problem with Preemption, demonstrating the use of semaphores and mutexes for synchronization and mutual exclusion between threads.



