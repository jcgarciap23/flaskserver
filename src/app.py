from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId 
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)

CORS(app)

#Configuración de la base de datos
app.config['MONGO_URI']='mongodb+srv://jcgarciap23:jcgarciap23@cluster0.qrp5d.mongodb.net/<dbname>?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/api/desechos/create', methods=['POST'])
def create():
    id = mongo.db.inforecogidas.insert(
        {
            'nombre': request.form['nombre'],
            'numero': request.form['numero'],
            'correo': request.form['correo'],
            'direccion': request.form['direccion'],
            'tipoDesecho': request.form['tipoDesecho']
        }
    )
    return jsonify(str(ObjectId(id)))

@app.route('/api/desechos/list', methods=['GET'])
def read():
    users = mongo.db.infodesechos.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/api/desechos/<id>', methods=['GET'])
def readIdinfo(id):
    info = mongo.db.infodesechos.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(info)
    return Response(response, mimetype="application/json")

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'No encontrado: '+request.url,
        'status': 404
    })
    return response.status_code

if __name__=="__main__":
    app.run(debug=True)





