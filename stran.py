from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'To je moja spletna stran'

app.run(host='0.0.0.0', port=8080)