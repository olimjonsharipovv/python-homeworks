#1
def uncommon_elements(list1, list2):
    from collections import Counter
   
    count1 = Counter(list1)
    count2 = Counter(list2)
  
    uncommon = []
    for element in set(list1 + list2):
        diff = abs(count1.get(element, 0) - count2.get(element, 0))
        uncommon.extend([element] * diff)
    return uncommon


print(uncommon_elements([1, 1, 2], [2, 3, 4]))  
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 

#2
def print_squares(n):
    for i in range(1, n):
        print(i**2)

print_squares(6)

#3
def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0
    while i < len(txt):
        result.append(txt[i])
        
        if (i + 1 < len(txt)) and (txt[i] in vowels or (i > 0 and result[-1] == '_')):
            pass
        elif (i + 1) % 3 == 0 and (i + 1) != len(txt):
            result.append('_')
        i += 1
    return ''.join(result)


print(insert_underscores("hello"))  
print(insert_underscores("assalom")) 
print(insert_underscores("abcabcdabcdeabcdefabcdefg")) 

#4
import random

def a():
    number = random.randint(1, 10)
    attempts = 10
    while attempts > 0:
        guess = int(input("Guess the number (1-10): "))
        if guess == number:
            print("You guessed it right!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
    else:
        print(f"You lost. The number was {number}.")
        play_again = input("Want to play again? (Y/YES/y/yes/ok): ").strip().lower()
        if play_again in ['y', 'yes', 'ok']:
            a()

a()























