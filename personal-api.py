from flask import Flask

app = Flask(__name__)

@app.route('/name')
def name():
    return "VARUNA PRIYA S"

@app.route('/register_number')
def register_number():
    return "22IT052"

@app.route('/department')
def department():
    return "INFORMATION TECHNOLOGY"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
