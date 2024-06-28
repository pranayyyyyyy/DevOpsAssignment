from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    print("This is the home page.")
    return "Welcome to the home page!"


@app.route('/login')
def login():
    print("This is the login page.")
    return "ffefewf."


@app.route('/details')
def details():
    print("This is the details page.")
    return "This is the details page."


@app.route('/About')
def About():
    print("This is the About page.")
    return "This is the About page."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
