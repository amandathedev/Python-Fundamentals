'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
my_list = []

for x in range(0, 50, 10):
    # for y in range(1, 10):
        # print(x, x + y)
    print(x, x + 1, x + 2, x + 3, x + 4, x + 5, x + 6, x + 7, x + 8, x + 9) 

# for x in range(0, 10, 10):
#     for y in range(1, 10):
#         my_list.append(x + y)
#     # print(my_list)
#     #     print(x, x + y, x + y)
#         print(x, x + 1, x + 2, x + 3, x + 4, x + 5, x + 6, x + 7, x + 8, x + 9)