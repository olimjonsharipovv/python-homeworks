def join_words(words, separator):
    return separator.join(words)
words = input("Enter a list of words separated by spaces:").split()
separator = input("Enter the separatot character (e.g., '-' or ','):")
result = join_words(words, separator)

print('Joined string:', result)










