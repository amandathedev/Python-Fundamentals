'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

sentence = input("Enter a sentence: ")
word_list = sentence.split()

chars = []
for x in word_list:
    chars.append(tuple(x))

print(chars)

# sentence = list(map(tuple, sentence.split()))
# print(sentence)