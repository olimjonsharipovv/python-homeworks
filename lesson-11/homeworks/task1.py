
import sqlite3

def create_database():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Roster
                      (Name TEXT, Species TEXT, Age INTEGER)''')

    initial_data = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    cursor.executemany('INSERT INTO Roster VALUES (?, ?, ?)', initial_data)
    conn.commit()
    print("Database created and initial data inserted.")

def update_data():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    conn.commit()
    print("\nUpdated Jadzia Dax to Ezri Dax.")

def query_bajorans():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    bajorans = cursor.fetchall()
    
    print("\nBajoran Characters:")
    for name, age in bajorans:
        print(f"Name: {name}, Age: {age}")

def delete_old_characters():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    conn.commit()
    print("\nDeleted characters older than 100 years.")

def add_rank_column():
    conn = sqlite3.connect('roster.db')

    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    
    # Update ranks
    ranks = [
        ('Benjamin Sisko', 'Captain'),
        ('Ezri Dax', 'Lieutenant'),
        ('Kira Nerys', 'Major')
    ]
    cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", 
                       [(rank, name) for name, rank in ranks])
    conn.commit()
    print("\nAdded Rank column and populated data.")

def query_sorted_by_age():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC")
    characters = cursor.fetchall()
    
    print("\nCharacters sorted by age (descending):")
    print("{:<20} {:<10} {:<5} {}".format("Name", "Species", "Age", "Rank"))
    print("-" * 45)
    for name, species, age, rank in characters:
        print(f"{name:<20} {species:<10} {age:<5} {rank}")

def main():
    # Execute all tasks in order
    create_database()
    update_data()
    query_bajorans()
    delete_old_characters()
    add_rank_column()
    query_sorted_by_age()

if __name__ == "__main__":
    main()











