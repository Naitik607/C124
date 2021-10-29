from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        "Name": "Raju",
        "Contact":"123456",
        "done":"False",
        "id":1
    },
    {
        "Name": "Rahul",
        "Contact":"654321",
        "done":"False",
        "id":2
    }
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    contact = {
        'id': tasks[-1]['id']+1,
        'Name': request.json('Name'),
        'Contact': request.json.get('Contact',""),
        'done':False
    }
    if request.json:
        return jsonify({
        "status": "added",
        "message":"Task added succesfully"
    })
    tasks.append(contact)

# type after the / "get-data"
@app.route("/get-data",methods=["GET"])
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)