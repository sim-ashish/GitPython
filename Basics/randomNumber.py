''' Python does not have a random() function to make a random number, 
    but Python has a built-in module called random that can be used to make random numbers'''

'''As the name suggest it will give us a random number everytime we execute this function'''

import random       # we have to import random so that we can use random() function


print(random.random())  # This will return us float value from 0 to 1

''' We are writing random.random() because the random module(script) containing the random function,
    if we import : from random import random 
    so we only do print(random())'''

print(random.uniform(20, 60)) # Return a random number between, and included, 20 and 60

print(random.randint(1,100)) # It will give us a random integer Value between 1 and 100 both include
print(random.randrange(3,9)) # It will give random integer between 1 (included) and 9 (not included)


'''We can use random module to choose an item from list also'''
mylist = ['Apple', 'Banana', 'Orange']  # We will discuss list later in detail

print(random.choice(mylist))

random.shuffle(mylist) # This function will shuffle the List
print(mylist)


''' There is seed() function in random module which is very helpful, if we are developing the program and want a predefined value'''
random.seed(20) # It will take a number as a argument and based on this number it generates random numbers 

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

# Above Print statements will give same result everytime

''' Without setting a seed, the RNG (Random Number Generator) uses system time or another source of entropy, leading to unpredictable sequences'''

random.seed(None) # It resets the generator to a system-entropy-based seed