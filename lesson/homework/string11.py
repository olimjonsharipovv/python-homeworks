def contains_digits(s):
    return any(char.isdigit() for char in s)

a = input("Enter a string: ")

if contains_digits(a):
    print("Sting contains digits.")
else:
    print("String does not contains digits")
    













