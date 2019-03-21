'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

my_string = input("Enter a phrase: ")

vowels = 0
for letter in my_string:
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        vowels += 1

print(f"There are {vowels} vowels in that sentence.")