user_string = input("Enter a string: ")
start_word = input("Enter the word to check if the string starts with: ")
end_word = input("Enter the word to check if the string ends with: ")

starts_with = user_string.startswith(start_word)
ends_with = user_string.endswith(end_word)

if starts_with and ends_with:
    print(f"The string starts with '{start_word}' and ends with '{end_word}'.")
elif starts_with:
    print(f"The string starts with '{start_word}' but does not end with '{end_word}'.")
elif ends_with:
    print(f"The string does not start with '{start_word}' but ends with '{end_word}'.")
else:
    print(f"The string neither starts with '{start_word}' nor ends with '{end_word}'.")





