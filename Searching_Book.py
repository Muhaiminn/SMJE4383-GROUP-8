class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# Function to search books by title
def search_by_title(books, title_query):
    found_books = [book for book in books if title_query.lower() in book['title'].lower()]
    return found_books

# Function to search books by author
def search_by_author(books, author_query):
    found_books = [book for book in books if author_query.lower() in book['author'].lower()]
    return found_books

# Sample database of books
books = [
    {'title': 'Python Programming', 'author': 'John Smith', 'price': 25.99},
    {'title': 'Data Science Handbook', 'author': 'Emily Davis', 'price': 30.50},
    {'title': 'Web Development Basics', 'author': 'Chris Johnson', 'price': 20.00},
    {'title': 'Machine Learning', 'author': 'Emily Davis', 'price': 28.00},
    {'title': 'Algorithms and Data Structures', 'author': 'Robert Johnson', 'price': 22.50}
]

# Sample usage: Search for books by title or author
search_option = input("Search by (1)Title or (2)Author: ")

if search_option == '1':
    title_query = input("Enter title to search: ")
    results = search_by_title(books, title_query)
elif search_option == '2':
    author_query = input("Enter author to search: ")
    results = search_by_author(books, author_query)
else:
    print("Invalid option selected.")
    results = []

if results:
    print("Search Results:")
    for book in results:
        print(f"Title: {book['title']}, Author: {book['author']}, Price: RM{book['price']}")
else:
    print("No books found.")
