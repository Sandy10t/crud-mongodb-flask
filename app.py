from flask import Flask, request, json
from bson.objectid import objectId
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('config.py')
mongo = PyMongo(app)

# def createConnection():
#    connection = mong("mongodb://localhost:27017")
#    db = connection.flask_db
#    return db

@app.route('/menu', methods = ['GET'])
def getmenu():
  menuData = list(mongo.db.menu.find({}))
  return object.__str__(menuData)

@app.route('/menu', methods = ['POST'])
def createmenu():
   data = json.loads(request.data)
   menuData = mongo.db.menu.insert_one(data)
   return 'Menu added successfully'
  
@app.route('/menu', methods = ['PUT'])
def updatemenu():
   # id = request.args.get('id')
   data = json.loads(request.data)
   menuData = mongo.db.menu.update_one({ 'name': name }, {"$set": data})
   return "Menu updated successfully"

@app.route('/menu', methods = ['DELETE'])
def deletemenu():
  # id = request.args.get('id')
  deleteQuery= {"_id": objectId(id)}
  menuData = mongo.db.menu.delete_one(deleteQuery)
  return "Menu deleted successfully"


if __name__ == '__main__':
   app.run()
