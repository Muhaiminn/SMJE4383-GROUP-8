from flask import Flask, render_template, request, redirect, url_for, g
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)
DATABASE = 'users.db'

def connect_db():
    """Connect to the SQLite database."""
    db_path = '/home/muhaimin01/users.db'
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

def get_db():
    """Get the SQLite database connection."""
    if 'db' not in g:
        g.db = connect_db()
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Close the SQLite database connection at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

def create_table():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                password TEXT
            )
        ''')
        connection.commit()

# Function to insert a new user into the database
def add_user(new_id, hashed_password):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO users (id, password) VALUES (?, ?)', (new_id, hashed_password))
            connection.commit()
        except sqlite3.IntegrityError:
            # ID already exists, handle it as needed
            return False
    return True

books = [
    {'id': 1, 'title': 'Python Programming', 'author': 'John Smith', 'genre':'Education', 'price': 26.00, 'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSrVHQJsUyhCZu6etQR9H1hOLVHbIikk_VgDlNdgvs8LnCIEA6gRF9_e-VvU55YjXNKYjCVL7ySH3wvAJOtGDeZzAI8I4MghoDk804vOd0du6Q4IiJUOHZL&usqp=CAE.jpg'},
    {'id': 2, 'title': 'Data Science Handbook', 'author': 'Emily Davis', 'genre':'Education', 'price': 30.50, 'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTFYkqhTgYHbAk1sK18O5cKD2GG2GwyvpUH30q-CDiihA7HJrrjvyVAzbk00U2HyIHxOd07FxKtaCvdTEc_haj_uuKY9UlJVnjI8wqGGVPK&usqp=CAE.jpg'},
    {'id': 3, 'title': 'Web Development Basics', 'author': 'Chris Johnson', 'genre':'Education', 'price': 20.00, 'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQLKSpbECMrljDpNt0lumEd_2vq65JO63YeMvC-jPZK-pAm-YJvYKzyD4zJZqwKratRNH_c0QwC0XMRG6VNMTC_UiGJQDrD0F9ilfIn1GeI&usqp=CAE.jpg'},
    {'id': 4, 'title': 'Machine Learning', 'author': 'Emily Davis', 'genre':'Education', 'price': 28.00, 'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTVsH1zKXupZWP7X5ZXUonDaJeYsaCnn2bYmSwk-0lUDNVL_uY_Ly3hOASxw4vnfDVaRM-5fae9GiiqBATX2CvXaTIHKN7JRE1QsCx9C71oENCgGiohYwQr&usqp=CAE.jpg'},
    {'id': 5, 'title': 'Algorithms and Data Structures', 'author': 'Robert Johnson', 'genre':'Education', 'price': 22.50, 'image': 'https://www.freetechbooks.com/uploads/1468389391-Toolbox_rs.jpg'},
    {'id': 6, 'title': 'Harry Potter and the Cursed Child: Parts One and Two Playscript', 'author': 'J.K. Rowling', 'genre':'Fantasy', 'price': 55.00 , 'image': 'https://m.media-amazon.com/images/I/91bUfxdDjWL._AC_UF1000,1000_QL80_.jpg'},    
    # Add more books as needed
]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        user_id = request.form.get('id')
        password = request.form.get('password')

        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()

            if user and bcrypt.check_password_hash(user[1], password):
                # Login successful
                return redirect(url_for('book'))
            else:
                # Invalid credentials
                return "Invalid credentials"

    return render_template('login.html')

# New route for sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign-up logic here
        new_id = request.form.get('new_id')
        new_password = request.form.get('new_password')

        # Hash the password before saving it
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        # Add the new user to the database
        add_user(new_id, hashed_password)

        # Redirect to the login page after successful sign-up
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout', methods=['POST'])
def logout():
    global authenticated_user
    authenticated_user = None  
    return redirect(url_for('login'))

@app.route('/search')
def search():
    query = request.args.get('query')
    # Perform search logic based on the query (e.g., filter available books by title or author)
    # This is a basic example; you might implement a more comprehensive search
    search_results = [book for book in books if (query.lower() in book['title'].lower() or query.lower() in book['author'].lower()) and book.get('availability', True)]
    return render_template('available_books.html', books=search_results)

@app.route('/book')
def book():
    return render_template('available_books.html', books=books)

@app.route('/checkout', methods=['POST'])
def checkout():
    selected_books_ids = request.form.getlist('selected_books')
    selected_books = [book for book in books if str(book['id']) in selected_books_ids]
    total_price = sum(book['price'] for book in selected_books)
    return render_template('checkout.html', selected_books=selected_books, total_price=total_price)

@app.route('/payment', methods=['POST'])
def payment():
    payment_option = request.form.get('payment_option')
    if payment_option in ['touch_n_go', 'debit_card']:

        return render_template('payment_success.html')
    else:
        return "Error: Invalid payment option selected"



if __name__ == '__main__':
    create_table()
    app.run(debug=True)

