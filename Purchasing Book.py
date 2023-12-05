class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, book, quantity=1):
        self.items.append({'book': book, 'quantity': quantity})

    def remove_from_cart(self, book):
        for item in self.items:
            if item['book'] == book:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['book'].price * item['quantity']
        return total

    def checkout(self):
        total = self.calculate_total()
        print("Total amount to be paid: RM{}".format(total))
        # Here you might implement payment processing, confirmation, etc.

# Creating available books
available_books = [
    Book("Python Programming", "John Smith", 25.99),
    Book("Data Science Handbook", "Emily Davis", 30.50),
    Book("Web Development Basics", "Chris Johnson", 20.00)
]

# Displaying available books for selection
print("Available Books:")
for i, book in enumerate(available_books):
    print(f"{i + 1}. {book.title} by {book.author} - RM{book.price}")

# User input for book selection
selected_book_index = int(input("Enter the number of the book you want to purchase: ")) - 1

if 0 <= selected_book_index < len(available_books):
    selected_book = available_books[selected_book_index]

    # Creating a shopping cart
    cart = ShoppingCart()

    # Adding selected book to the cart
    cart.add_to_cart(selected_book)

    # Displaying total and checking out
    cart.checkout()
else:
    print("Invalid book selection. Please choose a number within the range.")
