from flask import Flask, request
from flask.json import jsonify 

app = Flask(__name__)
@app.route("/")

def hello_world():
    return "hello_world"

contacts = [
    {
        'Id' : 1,
        'contact_no.' : 'This is contact 1.',
        'name' : '',
        'done' : False
    },
    {
        'Id' : 2,
        'contact_no.' : 'This is contact 2.',
        'name' : '',
        'done' : False
    }
]

@app.route("/get-data")

def get_contact():
    return jsonify({
        "data" : contacts
    })

@app.route("/add-data", methods = ["POST"])

def post_contact():
    if not request.json:
        return jsonify({
            'Status' : 'error',
            'Message' : 'please provide some data'
        }, 400
        )
    contact = {
       'Id' : contacts[-1]['Id']+1,
       'contact_no.' : request.json.get('contact_no.', ""),
       'name' : request.json['name'],
       'done' : False
    }
    contacts.append(contact)
    return jsonify({
        'Status' : 'success',
        'Message' : 'contacts added successfully'
    })

if (__name__ == '__main__'):
   app.run(debug = True)