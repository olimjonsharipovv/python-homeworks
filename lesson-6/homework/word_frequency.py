
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

def generate_report(word_counts):
    
    total_words = sum(word_counts.values())
    top_5_words = word_counts.most_common(5)
    
  
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} time{'s' if count > 1 else ''}")
       
    with open(OUTPUT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_5_words:
            file.write(f"{word} - {count}\n")
    print(f"Report saved to '{OUTPUT_FILE}'.")

def main():
    
    if not os.path.exists(INPUT_FILE):
        create_sample_file()
    
    word_counts = count_word_frequency()
    generate_report(word_counts)

if __name__ == "__main__":
    main()














