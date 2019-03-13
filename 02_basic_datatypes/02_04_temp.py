'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
fahrenheit = input("What is the temperature in Fahrenheit?  ")
celsius = (int(fahrenheit) - 32) * (5 / 9)
celsius = round(celsius, 1)

print(str(fahrenheit) + " degrees Fahrenheit = " + str(celsius) + " degrees Celsius.")