'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month = input("Please enter a number from 1 to 12: ")

month = int(month)

if month == 1:
    print("The first month of the year is January.")
elif month == 2:
    print("The second month of the year is February.")
elif month == 3:
    print("The third month of the year is March.")
elif month == 4:
    print("The fourth month of the year is April.")
elif month == 5:
    print("The fifth month of the year is May.")
elif month == 6:
    print("The sixth month of the year is June.")
elif month == 7:
    print("The seventh month of the year is July.")
elif month == 8:
    print("The eighth month of the year is August.")
elif month == 9:
    print("The ninth month of the year is September.")
elif month == 10:
    print("The tenth month of the year is October.")
elif month == 11:
    print("The eleventh month of the year is November.")
elif month == 12:
    print("The twelfth month of the year is December.")
else:
    print("Please enter a valid number from 1 to 12.")