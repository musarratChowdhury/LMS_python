import csv
from Book import Book
from Member import Member
from datetime import datetime


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Library Book Records:")
            for book in self.books:
                print(book)

    def display_members(self):
        if not self.members:
            print("No members registered in the library.")
        else:
            print("Library Member Records:")
            for member in self.members:
                print(member)

    def search_book(self, search_term):
        found_books = [book for book in self.books if
                       search_term.lower() in book.title.lower() or search_term.lower() == book.isbn.lower()]
        if found_books:
            print(f"Search Results for '{search_term}':")
            for book in found_books:
                print(book)
        else:
            print(f"No book found with Title or ISBN '{search_term}'.")

    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def remove_book(self, search_term):
        for book in self.books:
            if search_term.lower() == book.title.lower() or search_term.lower() == book.isbn.lower():
                self.books.remove(book)
                print(f"Book '{book.title}' removed successfully.")
                return
        print(f"No book found with Title or ISBN '{search_term}'.")

    def issue_book(self, member_id, book_title):
        member = self.search_member(member_id)
        if not member:
            print(f"No member found with ID '{member_id}'.")
            return

        for book in self.books:
            if book.title.lower() == book_title.lower():
                member.borrow_book(book, datetime.now())
                self.books.remove(book)
                print(f"Book '{book.title}' issued to '{member.name}'.")
                return

        print(f"No book found with title '{book_title}'.")

    def return_book(self, member_id, book_title):
        member = self.search_member(member_id)
        if not member:
            print(f"No member found with ID '{member_id}'.")
            return

        returned_book = None
        for borrowed_book, issue_date in member.borrowed_books:
            if borrowed_book.title.lower() == book_title.lower():
                returned_book = borrowed_book
                break

        if returned_book:
            return_date = datetime.now()
            delta = (return_date - issue_date).days
            fine = max(0, delta - 14) * 0.50  # Example fine: $0.50 per day after 14 days

            if fine > 0:
                print(f"Book '{returned_book.title}' returned late. Fine: ${fine:.2f}")
                member.add_fine(fine)
            else:
                print(f"Book '{returned_book.title}' returned on time.")

            member.return_book(returned_book)
            self.books.append(returned_book)
        else:
            print(f"Book '{book_title}' was not borrowed by '{member.name}'.")

    def generate_reports(self):
        print("\nLibrary Report:")
        print("Total Books in Library:", len(self.books))
        print("Total Members:", len(self.members))
        print("Books Issued to Members:")
        for member in self.members:
            if member.borrowed_books:
                print(f"\n{member.name} (ID: {member.member_id}):")
                for book, issue_date in member.borrowed_books:
                    print(f"- {book.title} (Issued on {issue_date.strftime('%Y-%m-%d')})")

    def save_to_csv(self, books_file='library_books.csv', members_file='library_members.csv'):
        # Save books
        with open(books_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Author', 'ISBN', 'Genre', 'Publication Date'])
            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, book.genre, book.publication_date])

        # Save members
        with open(members_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Member ID', 'Name', 'Contact', 'Join Date', 'Outstanding Fines'])
            for member in self.members:
                writer.writerow(
                    [member.member_id, member.name, member.contact, member.join_date, member.outstanding_fines])
                for book, issue_date in member.borrowed_books:
                    writer.writerow(
                        ['Borrowed Book', book.title, book.author, book.isbn, book.genre, issue_date.strftime('%Y-%m-%d')])
        print(f"Library records saved to '{books_file}' and '{members_file}'.")

    def load_from_csv(self, books_file='library_books.csv', members_file='library_members.csv'):
        # Load books
        try:
            with open(books_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.books = [Book(row['Title'], row['Author'], row['ISBN'], row['Genre'], row['Publication Date']) for row in reader]
        except FileNotFoundError:
            print(f"No file named '{books_file}' found.")

        # Load members
        try:
            with open(members_file, mode='r') as file:
                reader = csv.DictReader(file)
                current_member = None
                for row in reader:
                    if row['Member ID'] and row['Member ID'] != 'Borrowed Book':
                        current_member = Member(row['Member ID'], row['Name'], row['Contact'], row['Join Date'])
                        current_member.outstanding_fines = float(row['Outstanding Fines'])
                        self.members.append(current_member)
                    elif row['Member ID'] == 'Borrowed Book' and current_member:
                        book = Book(row['Title'], row['Author'], row['ISBN'], row['Genre'], 'Unknown')
                        issue_date = datetime.strptime(row['Publication Date'], '%Y-%m-%d')
                        current_member.borrow_book(book, issue_date)
            print(f"Library records loaded from '{books_file}' and '{members_file}'.")
        except FileNotFoundError:
            print(f"No file named '{members_file}' found.")
