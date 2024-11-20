# For Loop
# is control flow statement for specifying iteration, which allows code to be executed.
# Use the "for loop" when you know exactly how many times you want to iterate.
# Whereas you use a While loop
#
from xmlrpc.client import Boolean

for i in range(10): # Range allows us to iterate by a certain value
    print(i) # prints 0 to 9

for i in range (1, 10, 2): # Start ranges from 1 to 10. Adding a third integer allows us to iterate by that value: "step"
    print(i)

# "Lists" is a collection of elements in a particular order. They can sort any type of data.

numbers = [1, 2, 3, 4, 5] # List of numbers
numbers.append(10) # Adds 10 to the end of the list
numbers.pop(2) # Removes the 3rd element in the list
fruits = ["apple, banana, orange"] # List of strings
Boolean = [True, False, True] # List of booleans

# Iterating through a list
fruit = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    fruit = fruits[i]
    print(fruits[i])


