
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def can_borrow(self):
        return len(self.borrowed_books) < 3
    
    def borrow_book(self, book):
        if not self.can_borrow():
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum of 3 books")
        self.borrowed_books.append(book)
        book.is_borrowed = True
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f"{self.name} did not borrow '{book.title}'")
        self.borrowed_books.remove(book)
        book.is_borrowed = False
    
    def __str__(self):
        return f"Member: {self.name} (Books borrowed: {len(self.borrowed_books)}/3)"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        self.books.append(Book(title, author))
    
    def add_member(self, name):
        self.members.append(Member(name))
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException("Not found")
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None
    
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member {member_name} not found")
            return
        
        try:
            book = self.find_book(book_title)
            if book.is_borrowed:
                raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed")
            member.borrow_book(book)
            print(f"{member_name}  borrowed '{book.title}'")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            print(f"Member {member_name} not found")
            return
        
        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"{member_name}  returned '{book.title}'")
        except BookNotFoundException as e:
            print(f"Error: {e}")
    
    def display_status(self):
        print("\nLibrary Status:")
        print("\nBooks:")
        for book in self.books:
            print(f"- {book}")
        
        print("\nMembers:")
        for member in self.members:
            print(f"- {member}")
            if member.borrowed_books:
                print("  Currently borrowing:")
                for book in member.borrowed_books:
                    print(f"  - {book.title}")

def test_library():
    library = Library()
    
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")
    library.add_book("Pride and Prejudice", "Jane Austen", )
    library.add_book("Martin Iden", "Jack London")
    
    library.add_member("Alice")
    library.add_member("Bob")
    library.add_member("Olimjon")
  
    library.display_status()
 
    print("\nTesting borrowing books:")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "1984")
    
    library.borrow_book("Alice", "Pride and Prejudice")
   
    library.borrow_book("Bob", "Moby Dick")
  
    library.borrow_book("Bob", "The Great Gatsby")
    
    library.borrow_book("Bob", "Pride and Prejudice")
    
    library.display_status()
 
    print("\nTesting returning books:")
    library.return_book("Alice", "The Great Gatsby")
    library.return_book("Bob", "Pride and Prejudice")
    
    library.return_book("Alice", "Pride and Prejudice")
 
    library.display_status()

if __name__ == "__main__":
    test_library()


















