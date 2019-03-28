'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
# Create a list of all the words
sentence = input("Enter a sentence: ")
new_list = sentence.split()

# print(new_list)
# for x in new_list:
#     new_list.sort()
# print(new_list)

#Loop through all the words to find the one with the most occurrences
max_occurrence = 0
# Loop through all the words
for word in new_list:
        # If the number of occurences of the word is more than the max occurrence
    if new_list.count(word) > max_occurrence:
        # Update max word to item with current highest occurrence
        max_word = word

        # Set max occurrence equal to the highest count so far
        max_occurrence = new_list.count(word)

print(int(max_word) + 1)


print(max_occurrence)