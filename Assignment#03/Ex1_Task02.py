# a Python program to find if a given string starts with a given character using Lambda.

given_string = "String"
given_character = "S"
given_character = "A"

starts_with = lambda string, char: string.startswith(char)

output = starts_with(given_string, given_character)

if output:
    print("Matched!")
else:
    print("Not Matched!")
