'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# Convert an int to a float
number = input("Enter an integer. ")
number = float(number)

print(str(number))

# Convert a float to an int
number2 = int(number)
print(number2)

# Perform floor division using a float and an int
number3 = number // number2
print(number3)

# Use two user inputted values to perform multiplication
houses = input("How many houses are on your street? ")
streets = input("How many streets are in your neighborhood? ")

neighborhood = int(houses) * int(streets)
print("There are " + str(neighborhood) + " houses in your neighborhood.")