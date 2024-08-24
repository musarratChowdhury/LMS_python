class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre} Publication Date: {self.publication_date}"
