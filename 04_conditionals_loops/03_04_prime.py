'''
Print out every prime number between 1 and 100.

'''

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num % i == 0):
            prime = False
    if prime:
        print(num)