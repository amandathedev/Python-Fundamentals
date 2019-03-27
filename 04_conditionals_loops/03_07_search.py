'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

num = input("Enter a number from 0 to 1,000,000,000: ")
num = int(num)

search = 0
while num != search:
    print(search)
    search += 1
    if search == num:
        print("I found it.")
        break