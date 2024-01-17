#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response,render_template,session,redirect,url_for
from flask_migrate import Migrate
from flask_restful import Api, Resource,marshal_with,fields

from flask_bcrypt import Bcrypt

from models import db, Plant,User

from flask_cors import CORS

from datetime import datetime,timedelta,timezone

app = Flask(__name__,template_folder='/home/arthur-codex/Documents/DEV/MORINGA/Phase3/SQL/Flask/Auth/server/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY']='secret_key'


app.json.compact = True

bcrypt=Bcrypt(app)

cors = CORS(app, resources={r"//*": {"origins": "http://localhost:3000"}})

migrate = Migrate(app, db)
db.init_app(app)

# api = Api(app)

plant_fields={
    'id':fields.Integer,
    'name':fields.String,
    'image':fields.String,
    'price':fields.Float,
}

user_fields={
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String,
    'password':fields.String,
}

logged_in_user=None

def isValidSession():
    time_in=session['time_in']
    time_now=datetime.now(timezone.utc)

    diff=time_now-time_in
    diff_seconds=diff.total_seconds()
    print(f'diff time={diff},in seconds={diff_seconds}')
    if diff_seconds >40:
        return False
    session['time_in']=datetime.now(timezone.utc)
    return True


@app.route("/")
def index():
   print(session)

   if 'user_id' not in session:
       return redirect(url_for('loging'))
   
   # Check if his session is still valid
   is_valid=isValidSession()
   
   print(is_valid)

   if not is_valid:
       return redirect(url_for('loging'))
   
   time_in=session['time_in']
   print(type (time_in))
   print(time_in)
   user=User.query.filter_by(id=session['user_id']).first()
   print(vars(user))

   return render_template('index.html',time_in=time_in,user=user)

@app.route("/about")
def about():
    pass

@app.route('/user/add', methods=['GET','POST'])
def add_user():

    print(request.method)
   
    if request.method == 'POST':
       
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        hasshed_password=bcrypt.generate_password_hash(password).decode('utf8')
        user=User(name=name,email=email,password=hasshed_password)
        db.session.add(user)
        db.session.commit()
        print(user)
    
    return render_template('sighnup.html')

@app.route('/user/login', methods=['GET','POST'])
def loging():
    if request.method=='POST':
       email=request.form.get('email')
       password=request.form.get('password')
       user=User.query.filter_by(email=email).first()

       if not user:
          return render_template('login.html',server_message='User not found try again')

       check_user=bcrypt.check_password_hash(user.password,password)
       
       print(check_user)

       if not check_user:
          return render_template('login.html',server_message='Password incorrect')

     
       print(vars(user))
       print(type(user))
       print(user.password)
       print(email,password)
       session['user_id']=user.id
       session['time_in']=datetime.now(timezone.utc)
      
       return redirect(url_for('index'))
       

    return render_template('login.html')
      


if __name__ == '__main__':
    app.run(port=5555, debug=True)



# class Plants(Resource):
    
#     @marshal_with(plant_fields)
#     def get(self):
#         plants=Plant.query.all()

#         print(plants)
#         return plants
    
#     @marshal_with(plant_fields)
#     def post(self):
#        print(request.get_json())
#        body=request.get_json()
        
#        keys=['name','image','price']

#        for key in keys:
#            if key in body:
#                print(f'Key:${key} is present in body')
#            else:
#                print(f'Missing key:${key}')
#                return {'error':True,'message':"Some fields are missing"},400
     
#        new_plant=Plant(name=body['name'],image=body['image'],price=body['price'])
#        db.session.add(new_plant)
#        db.session.commit()
#        return new_plant,201

# class PlantByID(Resource):
#     pass

#Sessions.
# class Users(Resource):
    
#     def post(self):
#         body=request.get_json()
#         user=User(name=body['name'],email=body['email'],password=body['password'])
#         db.session.add(user)
#         db.session.commit()
    
# api.add_resource(Plants,'/plants')
# api.add_resource(Users,'/users')

