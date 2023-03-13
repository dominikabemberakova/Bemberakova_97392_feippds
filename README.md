# Bemberakova_97392_feippds -01
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3102/)
[![License](https://img.shields.io/npm/l/@tandil/diffparse?color=%23007ec6)](https://github.com/dominikabemberakova/Bemberakova_97392_feippds/blob/main/LICENSE)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-blue.svg)](https://conventionalcommits.org)

# About 

This Python module implements the Dining Philosophers Problem using the token solution.

# Assignment
Your task for the third assignment is to implement one of the following solutions to the dining philosophers problem:

solution with introducing waiters/lefties
solution with token passing (philosopher with the token can eat, after finishing eating, passes the token to their neighbor)
Describe the implemented solution in detail and compare it with the solution using a waiter. Focus on the possibility of starvation in each solution. You can conduct experiments or provide reasoning to support your comparison. There are no limits to creativity. Create a branch 03 in your repository for this task. The source code must be compatible with Python 3.10 and use threads from the fei.ppds library.

The source code must:

1. contain a module header with a description of the module, author name, and license
2. be clearly documented: each function (or class and its methods) must contain a docstring in accordance with PEP 257
3. be commented to a reasonable extent. Only comment where necessary to understand the context.
4. be in accordance with PEP 8

Write the documentation in the README.md file in the 03 branch (not in the README.md file in the master/main branch). In the documentation, formulate the problem you are solving, how your code should be run, etc. (i.e. all the information that someone who randomly found your source code on the internet would need).

Commit your work regularly. Your commit messages must comply with the CC. Cite all sources used. The deadline for submission is Monday, March 13, 2023, at 11:59 pm. Your repository must contain this assignment by then. The scoring for the assignment is as follows: 1 point for implementation, 1 point for documentation, 3 points for comparison. Try to be concise but informative.

The implementation of the solution with a waiter is available in the exercise examples repository.

# Problem solution:
The Dining Philosophers problem is a classic synchronization problem, where a group of philosophers sit around a table and each of them needs to use two forks to eat their meal. The problem is to design a protocol that the philosophers can follow to avoid deadlocks, where each philosopher is holding one fork and waiting for another to become available.

# Dining Philosophers Problem with Token Solution
This module implements the Dining Philosophers Problem with a solution that uses a token. The Dining Philosophers Problem is a classic synchronization problem that arises in computer science. It involves a group of philosophers who are sitting at a round table and trying to eat their meals. The problem is that there are only a limited number of forks available, so the philosophers must share them. However, they cannot share a fork with their immediate neighbor, as they need two forks to eat.

## Token Solution
The token solution involves introducing a token that is passed around the table. A philosopher can only eat when they hold the token, and they can only obtain the token when they have both forks. When a philosopher finishes eating, they pass the token to their neighbor. This ensures that only one philosopher is eating at a time, and that everyone eventually gets a turn.

## Solution using a waiter

The second implementation presented here uses a waiter system, where a waiter represented by a Semaphore is responsible for controlling access to the forks. The Shared class contains a waiter semaphore and an array of forks, each of which is a Mutex object. In each cycle of the philosopher's life, the philosopher first thinks and then tries to acquire the waiter semaphore. If the semaphore is full (i.e., all the forks are in use), the philosopher waits until a fork becomes available. If the semaphore is not full, the philosopher acquires two forks, eats, and then releases the forks and signals the waiter semaphore to release a waiting philosopher. This implementation is more efficient than the token-based solution since philosophers do not need to wait for the token to be released, but it requires more complex synchronization with the waiter semaphore.

## Summary

In summary, both implementations the token-based and waiter-based solutions are correct and solve the Dining Philosophers problem by controlling access to shared resources (forks). The token-based solution is simpler but less efficient, while the waiter-based solution is more complex but more efficient.

# Implementation Details

This module implements the Dining Philosophers Problem using the token solution. It uses the `Thread, Mutex, and print` classes from the `fei.ppds module`.  
# Functions 
I used the algorithm that was shown to us in the exercise.

## Shared class

The `Shared class` represents shared data for all threads, including an array of mutexes to represent the forks, a token holder, and a mutex to protect the token holder variable.

```python
class Shared:
    """Represent shared data for all threads."""
    def __init__(self):
        """Initialize an instance of Shared."""
        self.forks = [Mutex() for _ in range(NUM_PHILOSOPHERS)]
        self.token_holder: int = 0
        self.token_mutex: Mutex = Mutex()
```

## Eat and think functions

The `think and eat` functions simulate the philosopher thinking and eating, respectively. 

```python
def think(i: int):
    """Simulate thinking.

    Args:
        i -- philosopher's id
    """
    print(f"Philosopher {i} is thinking!")
    sleep(0.1)
```    

```python
def eat(i: int):
    """Simulate eating.

    Args:
        i -- philosopher's id
    """
    print(f"Philosopher {i} is eating!")
    sleep(0.1)
```

## The philosopher function 

The `philosopher` function is the main code that each philosopher runs. It first thinks, then it acquires the token before acquiring the two forks needed to eat. After eating, it releases the forks and the token. The main function initializes the shared data and creates a thread for each philosopher.

```python
def philosopher(i: int, shared: Shared):
    """Run philosopher's code.

    Args:
        i -- philosopher's id
        shared -- shared data
    """
    for _ in range(NUM_RUNS):
        think(i)
        # get token
        shared.token_mutex.lock()
        while shared.token_holder != i:
            shared.token_mutex.unlock()
            sleep(0.1)
            shared.token_mutex.lock()
        # get forks
        shared.forks[i].lock()
        shared.forks[(i+1) % NUM_PHILOSOPHERS].lock()
        shared.token_holder = (i + 1) % NUM_PHILOSOPHERS
        shared.token_mutex.unlock()
        eat(i)
        shared.forks[i].unlock()
        shared.forks[(i + 1) % NUM_PHILOSOPHERS].unlock()
```

## Printouts:

These are print statements that show the state of each philosopher during their execution in the dining philosophers problem.
The first set of print statements shows that all philosophers are initially thinking. Then, each philosopher starts eating one by one, as shown by the subsequent print statements that alternate between the philosopher's ID and the action "is eating!".
After each philosopher finishes eating, they start thinking again, which is shown by the print statements that alternate between the philosopher's ID and the action "is thinking!".
This sequence of actions (think -> eat -> think) is repeated for a certain number of runs specified by the constant NUM_RUNS.

```
Philosopher 0 is thinking!
Philosopher 1 is thinking!
Philosopher 2 is thinking!
Philosopher 3 is thinking!
Philosopher 4 is thinking!
Philosopher 0 is eating!
Philosopher 0 is thinking!
Philosopher 1 is eating!
Philosopher 1 is thinking!
Philosopher 2 is eating!
Philosopher 2 is thinking!
Philosopher 3 is eating!
Philosopher 3 is thinking!
Philosopher 4 is eating!
Philosopher 4 is thinking!
Philosopher 0 is eating!
Philosopher 0 is thinking!
Philosopher 1 is eating!
Philosopher 1 is thinking!
Philosopher 2 is eating!
Philosopher 2 is thinking!
Philosopher 3 is eating!
Philosopher 3 is thinking!
Philosopher 4 is eating!
Philosopher 4 is thinking!
```
