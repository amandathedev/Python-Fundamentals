'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
number_list = []

birthday = input("What day of the month were you born? ")
number_list.append(int(birthday))
age = input("How old are you? ")
number_list.append(int(age))
phone = input("What is your area code? ")
number_list.append(int(phone))
# address = input("What is your street address number? ")
# number_list.append(address)
# family = input("How many people are in your immediate family? ")
# number_list.append(family)
# money = input("How much money do you have in your wallet? ")
# number_list.append(money)
# shoe = input("What is your shoe size? ")
# number_list.append(shoe)
# pets = input("How many pets do you have? ")
# number_list.append(pets)
# rooms = input("How many rooms are in your house? ")
# number_list.append(rooms)
# tv = input("How many TV shows do you watch regularly? ")
# number_list.append(tv)


# for n in number_list:
#     print(n)
#     word_len.append((len(n), n))
#     print(len(n), n)
# word_len.sort()
print(max(number_list))

# Add total numbers
# list_sum = 0
# for x in number_list:
#     list_sum += x

# list_sum = sum(number_list)
# print(number_list)