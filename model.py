import app
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(project_dir, "shopbridge.db")}'
db = SQLAlchemy(app)

class Products(db.Model):
   id = db.Column('pid', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   description = db.Column(db.String(50))  
   price = db.Column(db.Iteger)
   quantity = db.Column(db.Integer)

   def __init__(self,name,description,price,quantity):
       self.name = name
       self.description = description
       self.price = price
       self.quantity = quantity