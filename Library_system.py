import csv

class Books:
    #All books in the library
    all_books = []

    #Outdated books
    outdated_books = []
    
    #Add new books to the library
    def __init__(self, book_name:str, book_ID:int, publish_year:int):
        #Assignment of the parameters
        self.book_name = book_name
        self.book_ID= book_ID
        self.publish_year = publish_year
        self.is_borrowed = False

        #Validation of the arguments
        assert publish_year >= 1900, 'Invalid input. Try again'
        assert type(book_name) == str, 'Input a proper book name'
        assert type(book_ID) == int, 'Input a proper book ID'
        assert type(publish_year) == int, 'Input a valid year'

       #Actions to excecute
        if self.publish_year < 2010:
            Books.outdated_books.append(self)
        else:
            Books.all_books.append(self) 

    #A way to permanently remove books
    def remove_book(self):
        Books.all_books.remove(self)

    @classmethod
    def list_from_bookfile(cls):
        with open('Books.csv', 'r') as bf:
            book_reader = csv.DictReader(bf)
            books = list(book_reader)

        for book in books:
          print(book)

        
    #Print readable output
    def __repr__(self):
        return f"(Book name: {self.book_name}, Book ID: {self.book_ID}, Publish year: {self.publish_year})\n"


class LibraryMember:
    def __init__(self, member_id:int, member_name:str):
        self.member_id = member_id
        self.name = member_name
        self.borrowed_books = []

        assert type(member_id) == int, 'Please input valid ID!'
        assert type(member_name) == str, 'Please input valid name!'

    def borrow_book(self, book):
        if not book.is_borrowed:
            if len(self.borrowed_books) == 2:
                print("You have reached the maximum borrowing limit!\n""Please return some books to be able to borrow this one")
            else:
                self.borrowed_books.append(book)
                book.is_borrowed = True
                print(f"{self.name} borrowed {book.book_name}.")
        else:
            print("Sorry, this book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{self.name} returned {book.book_name}.")
        else:
            print("You haven't borrowed this book.")


class LibraryStaff:
    raise_amt = 1.04
    def __init__(self, Staff_ID_no:int, Staff_name:str, Staff_pay:int):
        self.Staff_ID_no = Staff_ID_no
        self.Staff_name = Staff_name
        self.Staff_pay = Staff_pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
        return self.pay
    

class overdue_books(Books):
    def __init__(self, book_name:str, book_ID:int, publish_year:int, days_overdue=0):
        super().__init__(book_name, book_ID, publish_year)
        self.days_overdue = days_overdue

    def track_overdue_books(self):
        ls_overdue_books = [book for book in Books.all_books if book.is_borrowed]
        if ls_overdue_books:
            print(f'{self.book_name} is overdue')
        else:
            print('There are no overdue books')
