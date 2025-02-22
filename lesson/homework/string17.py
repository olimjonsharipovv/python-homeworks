a =input( "Enter a string: ")

vowels = "aeiouAEIOU"
symbol = "*"

result_string = ''.join([symbol if char in vowels else char for char in a])
print("The result after replacing vowels: ", result_string)














