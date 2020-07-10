from flask import Flask           # import flask
from models import Schema

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"if __name__ == "__main__":        # on running python app.py

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)  		  # running the app in debug mode  