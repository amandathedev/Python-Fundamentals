'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

low_num = input("Enter a number from 1 to 20: ")
low_num = int(low_num)
if low_num > 20 or low_num < 1:
	low_num = input("Please enter a number from 1 to 20: ")

high_num = input("Enter a number from 100 to 200: ")
high_num = int(high_num)
if high_num > 200 or high_num < 100:
	high_num = input("Please enter a number from 100 to 200: ")

my_sum = 0
for num in range(low_num, (high_num + 1)):
	my_sum += num
print("The sum is: " + str(my_sum))