

import os
import string
from collections import Counter

INPUT_FILE = "sample.txt"
OUTPUT_FILE = "word_count_report.txt"

def create_sample_file():
   
    print(f"'{INPUT_FILE}' does not exist. Please create it by typing a paragraph:")
    user_input = input("Enter your text: ")
    with open(INPUT_FILE, "w") as file:
        file.write(user_input)
    print(f"'{INPUT_FILE}' has been created.")

def clean_word(word):
    
    return word.strip(string.punctuation).lower()

def count_word_frequency():
   
    with open(INPUT_FILE, "r") as file:
        text = file.read()
        
    words = [clean_word(word) for word in text.split()]
    word_counts = Counter(words)
    
    return word_counts

def generate_report(word_counts, top_n):
    
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(top_n)
       
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} time{'s' if count > 1 else ''}")

    with open(OUTPUT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")
    print(f"Report saved to '{OUTPUT_FILE}'.")

def main():
   
    if not os.path.exists(INPUT_FILE):
        create_sample_file()
    
    word_counts = count_word_frequency()
        
    try:
        top_n = int(input("Enter the number of top common words to display: "))
        if top_n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    generate_report(word_counts, top_n)

if __name__ == "__main__":
    main()











