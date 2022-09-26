from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''Alfy Varghese\'s HW3

<p> sql_version_function() </p>'''
