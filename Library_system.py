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
        if publish_year < 1900:
            raise ValueError('Invalid input. Try again')
        if not isinstance(book_name, str):
            raise TypeError('Input a proper book name')
        if not isinstance(book_ID, int):
            raise TypeError('Input a proper book ID')
        if not isinstance(publish_year, int):
            raise TypeError('Input a valid year')


       #Actions to excecute
        if self.publish_year < 2010:
            Books.outdated_books.append(self)
        else:
            Books.all_books.append(self) 

    #A way to permanently remove books
    def remove_book(self):
        try:
            Books.all_books.remove(self)
        except ValueError:
            print(f"{self.book_name} is not in the list of all books.")

    @classmethod
    def list_from_bookfile(cls, filename='Books.csv'):
        with open(filename, 'r') as bf:
            book_reader = csv.DictReader(bf)
            for row in book_reader:
                try:
                    cls(book_name=row['book_name'].strip(), book_ID=int(row[' book_ID']), publish_year=int(row[' publish_year'].strip()))
                except (ValueError, TypeError) as e:
                    print(f"Error adding book from row {row}: {e}")



        
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
        self.Staff_pay = self.Staff_pay * self.raise_amt
        return self.pay
    

class overdue_books(Books):
    def __init__(self, book_name:str, book_ID:int, publish_year:int, days_overdue=0):
        super().__init__(book_name, book_ID, publish_year)
        self.days_overdue = days_overdue

    def track_overdue_books(self):
        ls_overdue_books = [book for book in Books.all_books if book.is_borrowed]
        if ls_overdue_books:
            print(f'{self.book_name} is overdue by {self.days_overdue} days')
        else:
            print('There are no overdue books')


Books.list_from_bookfile('Books.csv')