'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment = input("How much are you going to invest? ")
interest = input("What is the interest rate? ")
years = input("How many years are you toing to leave the investment to gain interest? ")

future_value = int(investment) * (float(interest) + 1) ** int(years)
future_value = round(future_value, 2)

print("In " + str(years) + " years at an interest rate of " + str(interest) + "%, your investment will become $" + str(future_value) +".")