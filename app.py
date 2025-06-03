from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/page2')
def page2():
    return send_from_directory('.', 'page2.html')

@app.route('/page3')
def page3():
    return send_from_directory('.', 'page3.html')

@app.route('/page4')
def page4():
    return send_from_directory('.', 'page4.html')

@app.route('/page5')
def page5():
    return send_from_directory('.', 'page5.html')

if __name__ == '__main__':
    app.run(debug=True)