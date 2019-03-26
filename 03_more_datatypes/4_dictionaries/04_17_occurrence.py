'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input = input("Enter a string: ")

chars = []
for x in user_input:
    chars.append(x)
print(chars)

# https://www.tutorialspoint.com/How-to-count-total-number-of-occurrences-of-an-object-in-a-Python-list
from collections import Counter
print(Counter(chars))

