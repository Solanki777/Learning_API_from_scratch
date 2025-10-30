from flask import Flask,jsonify,request

# create flask app
app=Flask(__name__)

# student data
students=[
    {"id":1, "Name":"Montu","Work":"Geograpy expert"},
    {"id":2,"Name":"Harpal","Work":"Farmer"}

]

@app.route('/')
def home():
    return jsonify(message="Welcome to student data")

@app.route('/students',methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    new_student=request.get_json()
    students.append(new_student)
    return jsonify({"message":"Student added","data":new_student}),201

@app.route('/students/<int:id>',methods=['PUT'])
def update_studetn(id):
    for s in students:
        if s['id']==id:
            s.update(request.get_json())
            return jsonify({"message":"DATA changed","data":s})
        else:
            return jsonify({"error":"student not found"}),404
        
@app.route('/student/<int:id>',methods=['DELETE'])
def delete_students(id):
    for s in students:
        if s['id']==id:
            students.remove(s)
            return jsonify({"messege":"student data deleted","data":s})
        else:
            return jsonify({"error":"student data not found"}),404


if __name__=='__main__':
    app.run(debug=True)
