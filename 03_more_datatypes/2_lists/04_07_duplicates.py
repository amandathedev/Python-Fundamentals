'''

Write a script that removes all duplicates from a list.

'''
my_list = ["a", "b", "a", "c", "c"]
print(my_list)
my_list = list(dict.fromkeys(my_list))
print(my_list)



# With help from https://www.w3schools.com/python/python_howto_remove_duplicates.asp