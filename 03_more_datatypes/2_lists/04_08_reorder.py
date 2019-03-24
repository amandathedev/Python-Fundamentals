'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
# Multiple inputs from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
my_list = list(map(int, input("Enter 10 numbers, separated by a space: "). split()))
print("List of numbers: ", my_list)

# Reordering https://stackoverflow.com/questions/2177590/how-can-i-reorder-a-list
my_order = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]
my_list = [my_list[i] for i in my_order]
print(my_list)