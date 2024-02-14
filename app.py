from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Shweta here! Python web application has been created using Azure Web app service!"
