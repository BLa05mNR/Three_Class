class Book:
    def __init__(self, title, author, year, pages, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def checkout(self):
        self.available = False

    def checkin(self):
        self.available = True


class Member:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.books = []

    def __str__(self):
        return self.name

    def checkout(self, book):
        if book.available:
            self.books.append(book)
            book.checkout()
            print(f"{self.name} checked out {book}")
        else:
            print(f"Sorry, {book} is not available")

    def checkin(self, book):
        if book in self.books:
            self.books.remove(book)
            book.checkin()
            print(f"{self.name} checked in {book}")
        else:
            print(f"{self.name} did not check out {book}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def checkout(self, member_name, book_title):
        for member in self.members:
            if member.name == member_name:
                for book in self.books:
                    if book.title == book_title:
                        member.checkout(book)

    def checkin(self, member_name, book_title):
        for member in self.members:
            if member.name == member_name:
                for book in self.books:
                    if book.title == book_title:
                        member.checkin(book)
