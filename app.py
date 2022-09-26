from flask import Flask
app = Flask(__name__)

@app.route('/hw3')
def index():
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
      <meta charset="utf-8">
      <title> Hw3 </title>
        </head>
        <body>
          <h1> Alfy Varghese\'s HW3</h1>
      <p> sql_version_function() </p>
        </body>
        </html>"""

if __name__ == "__main__":
    app.run()
