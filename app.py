from flask import Flask,jsonify

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


# if __name__ == '__main__':
#     app.run(debug=True)
