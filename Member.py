class Member:
    def __init__(self, member_id, name, contact, join_date):
        self.member_id = member_id
        self.name = name
        self.contact = contact
        self.join_date = join_date
        self.borrowed_books = []
        self.outstanding_fines = 0.0

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Contact: {self.contact}, Join Date: {self.join_date}, Borrowed Books: {len(self.borrowed_books)}, Outstanding Fines: ${self.outstanding_fines:.2f}"

    def borrow_book(self, book, issue_date):
        self.borrowed_books.append((book, issue_date))

    def return_book(self, book):
        for borrowed_book in self.borrowed_books:
            if borrowed_book[0] == book:
                self.borrowed_books.remove(borrowed_book)
                return borrowed_book
        return None

    def add_fine(self, amount):
        self.outstanding_fines += amount

    def pay_fine(self, amount):
        self.outstanding_fines = max(self.outstanding_fines - amount, 0)
