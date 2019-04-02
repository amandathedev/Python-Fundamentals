'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000
my_num = input("Please enter a number between 1 and 1,000,000,000: ")
my_num = int(my_num)
# calls a function that determines whether the number is divisible by both 4 and 7
def is_divisible():
    if my_num % 4 == 0 and my_num % 7 == 0:
        print("Your number is divisible by both 4 and 7.")
# calls a function that determines whether the number is divisible by 4 or 7
    # elif my_num % 4 == 0 or my_num % 7 == 0:
    #     print("Your number is divisible by either 4 or 7.")
# calls a function that determines whether the number is divisible by 4 or 7 exclusively
    elif my_num % 4 == 0 and my_num % 7 != 0:
        print("Your number is divisible by 4 but not 7.")
    elif my_num % 7 == 0 and my_num % 4 != 0:
        print("Your number is divisible by 7 but not 4.")
# print the results
    else:
        print("Your number is not divisible by 4 or 7.")

is_divisible()