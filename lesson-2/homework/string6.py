def contains_substring(main_string, substring):
    return substring in main_string

main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if contains_substring(main_string, substring):
    print(f"{main_string} contains {substring}")
else:
    print(f"{main_string} does not contains {substring}")    
    
    
    
    
    
    
    
    
    
    