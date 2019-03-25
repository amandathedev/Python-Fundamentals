'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

sentence = input("Enter a sentence: ")
# word_list = sentence.split()
# print(word_list)

# chars = []
# for x in sentence:
#     chars.append(x)
# print(chars)

# tuple_list = tuple(word_list)
# print(type(tuple_list))

sentence = list(map(tuple, sentence.split()))
print(sentence)