def find_factors(n):
   
    for i in range(1, n + 1):
        if n % i == 0:  
            print(f"{i} is a factor of {n}")

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        find_factors(num)
except ValueError:
    print("Invalid input. Please enter a positive integer.")





















