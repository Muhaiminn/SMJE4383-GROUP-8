from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'muhaimin': {'id': 'muhaimin', 'password': 'min'},
    'thana': {'id': 'thana', 'password': 'cha'},
    'ameera': {'id': 'ameera', 'password': 'meer'},
    'amir': {'id': 'amir', 'password': 'mir'},
    # Add more users as needed
}

authenticated_user = None

books = [
    {'id': 1, 'title': 'Python Programming', 'author': 'John Smith', 'price': 26.00, 'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSrVHQJsUyhCZu6etQR9H1hOLVHbIikk_VgDlNdgvs8LnCIEA6gRF9_e-VvU55YjXNKYjCVL7ySH3wvAJOtGDeZzAI8I4MghoDk804vOd0du6Q4IiJUOHZL&usqp=CAE.jpg'},
    {'id': 2, 'title': 'Data Science Handbook', 'author': 'Emily Davis', 'price': 30.50, 'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTFYkqhTgYHbAk1sK18O5cKD2GG2GwyvpUH30q-CDiihA7HJrrjvyVAzbk00U2HyIHxOd07FxKtaCvdTEc_haj_uuKY9UlJVnjI8wqGGVPK&usqp=CAE.jpg'},
    {'id': 3, 'title': 'Web Development Basics', 'author': 'Chris Johnson', 'price': 20.00, 'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQLKSpbECMrljDpNt0lumEd_2vq65JO63YeMvC-jPZK-pAm-YJvYKzyD4zJZqwKratRNH_c0QwC0XMRG6VNMTC_UiGJQDrD0F9ilfIn1GeI&usqp=CAE.jpg'},
    {'id': 4, 'title': 'Machine Learning', 'author': 'Emily Davis', 'price': 28.00, 'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTVsH1zKXupZWP7X5ZXUonDaJeYsaCnn2bYmSwk-0lUDNVL_uY_Ly3hOASxw4vnfDVaRM-5fae9GiiqBATX2CvXaTIHKN7JRE1QsCx9C71oENCgGiohYwQr&usqp=CAE.jpg'},
    {'id': 5, 'title': 'Algorithms and Data Structures', 'author': 'Robert Johnson', 'price': 22.50, 'image': 'https://www.freetechbooks.com/uploads/1468389391-Toolbox_rs.jpg'},
    # Add more books as needed
]

@app.route('/login', methods=['GET', 'POST'])
def login():
    global authenticated_user
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']
        print(f"Entered ID: {user_id}, Entered Password: {password}")  
        user = users.get(user_id)
        print(f"User Data: {user}")  
        if user and user['password'] == password:
            authenticated_user = user_id
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

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

@app.route('/')
def index():
    if not authenticated_user:
        return redirect(url_for('login'))
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
    app.run(debug=True, port=5000)

