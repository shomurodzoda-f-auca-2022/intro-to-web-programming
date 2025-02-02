class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def displayInfo(self):
        print(f"{self.__title} by {self.__author} ({self.__year}).")

class Library:
    def __init__(self):
        self.__books = []

    def addBook(self, book):
        self.__books.append(book)

    def listBooks(self):
        for book in self.__books:
            book.displayInfo()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To kill a Mockingbird", "Harper Lee", 1960)

library = Library()
library.addBook(book1)
library.addBook(book2)

library.listBooks()