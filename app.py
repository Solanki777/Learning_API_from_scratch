# first install python then flask inside your system to work with python libraries

from flask import Flask,jsonify
# # flask is lightweight web application framework to develop website
# Here Flask,&jsonify is a utility function used to create JSON responses easily and efficiently. It is particularly useful when building APIs, as it simplifies the process of returning JSON data to the client.

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to my first API")

@app.route('/info')
def info():
    data={
        "Name":"MAHESH",
        "College":"Shantilal Shah Engineering College",
        "City":"Bhavnagar"
    }
    return jsonify(data)
app.run()