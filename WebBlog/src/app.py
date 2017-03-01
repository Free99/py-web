__author__ = 'Tianshan'

from flask import Flask

app = Flask(__name__)  # '__main__'

@app.route('/')
def greatings():
    return "Hello, world!"

if __name__ == '__main__':
    app.run() # Default port is 5000, use (port=XXXX) to change it