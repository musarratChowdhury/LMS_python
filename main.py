from Library import  Library
from Book import Book
from Member import Member
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_books_issued_over_time(library):
    issue_dates = []
    for member in library.members:
        for book, issue_date in member.borrowed_books:
            issue_dates.append(issue_date.strftime('%Y-%m'))

    issue_counts = pd.Series(issue_dates).value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=issue_counts.index, y=issue_counts.values, marker="o", color="orange")
    plt.title('Books Issued Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Books Issued')
    plt.xticks(rotation=45)
    plt.show()

def plot_member_activity_distribution(library):
    active_members = sum(1 for member in library.members if member.borrowed_books)
    inactive_members = len(library.members) - active_members

    labels = ['Active Members', 'Inactive Members']
    sizes = [active_members, inactive_members]
    colors = ['#66b3ff', '#ff9999']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Member Activity Distribution')
    plt.show()

def plot_books_by_genre(library):
    genres = [book.genre for book in library.books]
    genre_counts = pd.Series(genres).value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette="viridis")
    plt.title('Number of Books by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Books')
    plt.xticks(rotation=45)
    plt.show()

def main(genre=None):
    library = Library()
    library.load_from_csv()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book Record")
        print("2. Add Member")
        print("3. Display Book Records")
        print("4. Display Member Records")
        print("5. Search Book Record")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Generate Reports")
        print("9. Plot Books by Genre")
        print("10. Plot Books Issued Over Time")
        print("11. Plot Member Activity Distribution")
        print("12. Save and Exit")
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author, isbn, genre, publication_date)
            library.add_book(book)
        elif choice == '2':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            contact = input("Enter contact information: ")
            join_date = input("Enter join date (YYYY-MM-DD): ")
            member = Member(member_id, name, contact, join_date)
            library.add_member(member)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            library.display_members()
        elif choice == '5':
            search_term = input("Enter book title or ISBN to search: ")
            library.search_book(search_term)
        elif choice == '6':
            member_id = input("Enter member ID: ")
            book_title = input("Enter book title to issue: ")
            library.issue_book(member_id, book_title)
        elif choice == '7':
            member_id = input("Enter member ID: ")
            book_title = input("Enter book title to return: ")
            library.return_book(member_id, book_title)
        elif choice == '8':
            library.generate_reports()
        elif choice == '9':
            plot_books_by_genre(library)
        elif choice == '10':
            plot_books_issued_over_time(library)
        elif choice == '11':
            plot_member_activity_distribution(library)
        elif choice == '12':
            library.save_to_csv()
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()





