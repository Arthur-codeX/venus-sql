#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource,marshal_with,fields

from models import db, Plant

from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

cors = CORS(app, resources={r"//*": {"origins": "http://localhost:3000"}})

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

plant_fields={
    'id':fields.Integer,
    'name':fields.String,
    'image':fields.String,
    'price':fields.Float,
}

class Plants(Resource):
    
    @marshal_with(plant_fields)
    def get(self):
        plants=Plant.query.all()

        print(plants)
        return plants
    
    @marshal_with(plant_fields)
    def post(self):
       print(request.get_json())
       body=request.get_json()
        
       keys=['name','image','price']

       for key in keys:
           if key in body:
               print(f'Key:${key} is present in body')
           else:
               print(f'Missing key:${key}')
               return {'error':True,'message':"Some fields are missing"},400
     
       new_plant=Plant(name=body['name'],image=body['image'],price=body['price'])
       db.session.add(new_plant)
       db.session.commit()
       return new_plant,201

class PlantByID(Resource):
    pass
    
api.add_resource(Plants,'/plants')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
