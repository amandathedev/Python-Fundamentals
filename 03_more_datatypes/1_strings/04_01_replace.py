'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

my_string = "Peter Piper picked a peck of pickled peppers."

my_string = my_string.lower()
new_string = my_string.replace('p', 'w')
print(f"The new string is {new_string}")