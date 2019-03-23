'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
my_list = []

string_1 = input("Tell me your name: ")
my_list.append(string_1)
string_2 = input("Tell me your dog's name: ")
my_list.append(string_2)
string_3 = input("Tell me your street name: ")
my_list.append(string_3)

print(my_list)

word_len = []
for n in my_list:
    word_len.append((len(n), n))
    print(word_len)
word_len.sort()
print(word_len)
print(word_len[-1][1])