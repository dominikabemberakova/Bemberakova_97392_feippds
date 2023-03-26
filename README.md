# Dining savages problem

Implement a program that solves the modified synchronization problem of Dinning Savages.

There are several cooks in a tribe. When a savage discovers that the pot is empty, he wakes up ALL the cooks, who can help each other in cooking and cook together. JUST ONE cook tells the waiting savage that it is done. The cook puts the portions in the pot, not the savage!

## Task
Your task for the fourth assignment is to implement one of the following solutions to the Dining Savages problem:

1. With one cook 8b
2. With multiple cooks 10b
All relevant information can be found in the assignment (see materials) and in the video [lecture](https://www.youtube.com/watch?v=54zi8qdBjdk)

### The source code must:

1. contain a module header with a module description, author name, and license
2. be clearly documented: each function (or class and its methods) must have a docstring in accordance with PEP 257
3. be adequately commented. Add comments only where necessary for understanding the context.
follow PEP 8 guidelines
4. Write the documentation in the README.md file in the 04 branch (not in the README.md file in the master/main branch). You can find the documentation content in the presentation as well.

Commit your work regularly, and your commit messages must be in accordance with CC. Cite all sources used. You have until Monday, March 27, 2023, at 11:59 pm to submit your assignment. Your repository must contain the given assignment by that time.

## Analysis:
Let it be understood that the original solution was explained at the lecture, and therefore we will not repeat the explanation. If necessary, I am adding a link to the [lecture](https://www.youtube.com/watch?v=iotYZJzxKf4&t=3996s).  

Let's move to the modification analysis. Modification requirements are:
1. There are several cooks in the tribe. 
2. When the savage discovers that the pot is empty, he wakes up ALL the cooks.
3. Cooks can help each other in cooking and cook together. 
4. JUST ONE cook tells the waiting savage that it is done. 
5. The cook puts the portions in the pot, not the savage!

To fulfill the first requirement, we add a list of cooks/threads to the program.
```python
cooks = [Thread(cook, shared, i) for i in range(COOKS)]
```

To meet the second requirement, we have to signal to ALL the cooks. This means we have to modify the savage method:

```python
shared.barrier2.wait(last=f"savage {i}: all of us are here, let's have dinner")
shared.mutex.lock()
print(f"savage {i}: num of servings in pot is {shared.servings}")
if shared.servings == 0:
    print(f"savage {i}: wakes all cooks")
    shared.empty_pot.signal(COOKS)    # <-- modify this part, from signal() to signal(COOKS)
    shared.full_pot.wait()
get_serving_from_pot(shared, i)
shared.mutex.unlock()
eat(i)
shared.barrier1.wait(last=" ")
```

The second requirement was fulfilled. Let's move to the third one which is that the cooks can help each other in cooking and cook together. Well, there are no further details stated, so we can basically let each of them cook for a certain time concurrently and then declare that all the food is done. This doesn't require any modifications.

Requirement number 4 says that JUST ONE cook tells the waiting savage that it is done. The ONE cook is the last one obviously because all the cooking has to be already done. We need a mechanism to tell which cook is the last one. 

We also need to make sure that there will be no overtaking. As mentioned, the empty_pot signalization will be made for all threads. Semaphore alone only ensures that N cooks will be let in, it doesn't make difference between the case where each cook will be let in once and the second case where one cook will be let in 5 times.

These two things can be achieved with the use of barrier. The barrier captures the case when the thread is last. By modifying the barrier wait function, we can achieve that we return a bool value whether the passing thread was last or not.

**Barrier wait modification:**
```python
def wait(self, each=None, last=None):
    self.mutex.lock()
    if each:
        print(each)
    self.count += 1
    is_last = False     # <-- inital value for every thread
    if self.count == self.threads_num:
        if last:
            print(last)
        self.count = 0
        is_last = True    # <-- change the value to true if it is last thread
        self.barrier.signal(self.threads_num)
    self.mutex.unlock()
    self.barrier.wait()
    return is_last    # return value.
```

Now we need to place the barrier in a correct position and execute the actions of the last thread. 

```python
while True:
    shared.empty_pot.wait()

    print(f"cook {i}: cooking")
    sleep(randint(50, 80) / 100)

    is_last = shared.barrier3.wait()    
    if is_last:
        put_servings_in_pot(shared, i)
        shared.full_pot.signal()
```

Why did we choose this placement? We have to perform the cooking and determine the last cook. This means that the barrier has to be placed between cooking and serving the pot. Based on the return value of the barrier, the last cook adds portions to the pot and signals that the pot is full. Barrier also ensures that there will be no overtaking because all the cooks have to cook their part before continuing. We have thus fulfilled conditions 4 and 5.

## Printouts:
Printouts will be displayed for 8 servings, 3 savages, and 5 cooks.

```
savage 1: all of us are here, let's have dinner
savage 1: num of servings in pot is 0
savage 1: wakes all cooks
cook 2: cooking
cook 3: cooking
cook 4: cooking
cook 0: cooking
cook 1: cooking
cook 3: all cooked, servings to pot
savage 1: takes from pot, portions left: 7
savage 1: feasting
savage 0: num of servings in pot is 7
savage 0: takes from pot, portions left: 6
savage 0: feasting
savage 2: num of servings in pot is 6
savage 2: takes from pot, portions left: 5
savage 2: feasting
 
savage 1: all of us are here, let's have dinner
savage 1: num of servings in pot is 5
savage 1: takes from pot, portions left: 4
savage 1: feasting
savage 0: num of servings in pot is 4
savage 0: takes from pot, portions left: 3
savage 0: feasting
savage 2: num of servings in pot is 3
savage 2: takes from pot, portions left: 2
savage 2: feasting
 
savage 1: all of us are here, let's have dinner
savage 1: num of servings in pot is 2
savage 1: takes from pot, portions left: 1
savage 1: feasting
savage 2: num of servings in pot is 1
savage 2: takes from pot, portions left: 0
savage 2: feasting
savage 0: num of servings in pot is 0
savage 0: wakes all cooks
cook 3: cooking
cook 0: cooking
cook 4: cooking
cook 2: cooking
cook 1: cooking
cook 2: all cooked, servings to pot
savage 0: takes from pot, portions left: 7
savage 0: feasting
 
savage 2: all of us are here, let's have dinner
savage 2: num of servings in pot is 7
savage 2: takes from pot, portions left: 6
savage 2: feasting
savage 1: num of servings in pot is 6
savage 1: takes from pot, portions left: 5
savage 1: feasting
savage 0: num of servings in pot is 5
savage 0: takes from pot, portions left: 4
savage 0: feasting
 
savage 1: all of us are here, let's have dinner
savage 1: num of servings in pot is 4
savage 1: takes from pot, portions left: 3
savage 1: feasting
savage 2: num of servings in pot is 3
savage 2: takes from pot, portions left: 2
savage 2: feasting
savage 0: num of servings in pot is 2
savage 0: takes from pot, portions left: 1
savage 0: feasting
 
savage 2: all of us are here, let's have dinner
savage 2: num of servings in pot is 1
savage 2: takes from pot, portions left: 0
savage 2: feasting
savage 0: num of servings in pot is 0
savage 0: wakes all cooks
cook 1: cooking
cook 3: cooking
cook 0: cooking
cook 4: cooking
cook 2: cooking
cook 2: all cooked, servings to pot
savage 0: takes from pot, portions left: 7
savage 0: feasting
savage 1: num of servings in pot is 7
savage 1: takes from pot, portions left: 6
savage 1: feasting
```

As you can see, the solution is correct and it meets all the requirements of the modification.

