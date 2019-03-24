'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
# https://www.tutorialspoint.com/How-to-join-list-of-lists-in-python
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flat_list = []
for i in starting_list:
    for j in i:
        flat_list.append(j)
print(flat_list)