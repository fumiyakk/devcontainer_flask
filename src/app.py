from flask import Flask, request
from datetime import datetime
import re
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
 
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)
 
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
 
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(address='0.0.0.0')
