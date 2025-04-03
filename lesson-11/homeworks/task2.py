
import sqlite3

def create_database():
    # Connect to database 
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Books
                      (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)''')

    initial_data = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    cursor.executemany('INSERT INTO Books VALUES (?, ?, ?, ?)', initial_data)
    conn.commit()
    print("Database created and initial data inserted.")

def update_data():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Update publication year of 1984
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    conn.commit()
    print("\nUpdated publication year of '1984' to 1950.")

def query_dystopian_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    dystopian_books = cursor.fetchall()
    
    print("\nDystopian Books:")
    for title, author in dystopian_books:
        print(f"Title: {title}, Author: {author}")

def delete_old_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    conn.commit()
    print("\nDeleted books published before 1950.")

def add_rating_column():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
 
    ratings = [
        ('To Kill a Mockingbird', 4.8),
        ('1984', 4.7),
        ('The Great Gatsby', 4.5)
    ]
    cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", 
                       [(rating, title) for title, rating in ratings])
    conn.commit()
    print("\nAdded Rating column and populated data.")

def query_sorted_by_year():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC")
    books = cursor.fetchall()
    
    print("\nBooks sorted by publication year (ascending):")
    print("{:<25} {:<20} {:<6} {:<12} {}".format("Title", "Author", "Year", "Genre", "Rating"))
    print("-" * 75)
    for title, author, year, genre, rating in books:
        print(f"{title:<25} {author:<20} {year:<6} {genre:<12} {rating}")

def main():
    create_database()
    update_data()
    query_dystopian_books()
    delete_old_books()
    add_rating_column()
    query_sorted_by_year()

if __name__ == "__main__":
    main()










