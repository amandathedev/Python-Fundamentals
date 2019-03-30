'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

# https://stackoverflow.com/questions/55433855/how-to-combine-list-of-dictionaries-based-on-key

for x in famous_quotes:
    print(f"\"{x['quote']}\" - {', '.join(reversed(x['full_name'].split()))}")

# quote_names = [k['full_name'] for k in famous_quotes]
# quote = [i['quote'] for i in famous_quotes]

# print(f"\"{quote[0]}\" - {quote_names[0]} ")
# print(f"\"{quote[1]}\" - {quote_names[1]} ")
# print(f"\"{quote[2]}\" - {quote_names[2]} ")
# print(f"\"{quote[3]}\" - {quote_names[3]} ")
# print(f"\"{quote[4]}\" - {quote_names[4]} ")
# print(f"\"{quote[5]}\" - {quote_names[5]} ")
# print(f"\"{quote[6]}\" - {quote_names[6]} ")