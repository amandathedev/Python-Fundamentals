'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
# https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe

from collections import Counter

dict_1 = Counter({"a": 1, "b": 2, "c": 3})
dict_2 = Counter({"a": 2, "c": 4 , "d": 2})

result = Counter(dict_1) + Counter(dict_2)

print(result)