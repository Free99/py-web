from flask import Flask, render_template

__author__ = 'Tianshan'


app = Flask(__name__)  # '__main__'

@app.route('/')
def greatings():
    return render_template('login.html')

if __name__ == '__main__':
    app.run() # Default port is 5000, use (port=XXXX) to change it