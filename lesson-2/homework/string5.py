def count_vowels_and_consonants(s):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    s = s.lower()
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(user_input)

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")







