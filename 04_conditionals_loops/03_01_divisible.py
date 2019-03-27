'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

number = input("Enter a number between 1 and 1,000,000,000: ")

number = int(number)

if number < 1:
    print("Please do not enter a negative number.")
elif number > 1000000000:
    print("Please choose a smaller number.")
elif number % 3 == 0:
    print("That number is divisible by 3.")
else:
    print("That number is not divisible by 3.")