from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def li():
    return render_template('login.html')

@app.route('/register')
def reg():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)

#db password lmaomysql