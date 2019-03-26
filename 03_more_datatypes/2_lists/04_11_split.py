'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = input("Enter a sentence: ")
new_list = sentence.split()

# print(new_list)
# for x in new_list:
#     new_list.sort()
# print(new_list)

for x in new_list:
    if new_list.count(x) > 1:
        print(x)