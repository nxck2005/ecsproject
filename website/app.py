import sqlite3
from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with your own key

# SQLite helper functions
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def find_user_by_reg_num(reg_num):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE reg_num = ?', (reg_num,)).fetchone()
    conn.close()
    return user

def create_user(reg_num, password):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (reg_num, password) VALUES (?, ?)', (reg_num, password))
    conn.commit()
    conn.close()

# Home route (accessible if logged in)
@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('index.html', user=session['user_id'])
    else:
        flash('Please log in to access this page', 'danger')
        return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        reg_num = request.form['reg_num']
        password = request.form['password']
        user_row = find_user_by_reg_num(reg_num)
        if user_row and user_row['password'] == password:
            session['user_id'] = user_row['id']
            session['user_reg_num'] = user_row['reg_num']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid registration number or password', 'danger')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_reg_num', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        reg_num = request.form['reg_num']
        password = request.form['password']
        if find_user_by_reg_num(reg_num):
            flash('Registration number already registered', 'danger')
        else:
            create_user(reg_num, password)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
