'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
# http://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/

import operator
input_dict = {"item1": 5, "item2": 6, "item3": 1}
print(input_dict)

result_list = sorted(input_dict.items(), key=operator.itemgetter(1))

print(result_list)