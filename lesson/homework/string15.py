a = input("Enter a sentence: ")
words = a.split()
acronym = "".join(word[0].upper() for word in words)


print("Acronym: ", acronym)
