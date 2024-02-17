from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://toxic_database.db'  # Update with your database URI
db = SQLAlchemy(app)


user_entries = db.Table('user_entries',
                        db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                        )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_data = db.relationship('Userdata', backref='User')
    entries = db.relationship('Entry', secondary='user_entries', backref='users')


class Userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    institution = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    pubchem_id = db.Column(db.String(10), nullable=False)
    chembl_id = db.Column(db.String(10), nullable=False)
    inchkey = db.Column(db.String(30), nullable=False)
    chemical_formula = db.Column(db.String, nullable=False)
    compound_name = db.Column(db.String(50), nullable=False)
    mol_weight = db.Column(db.Float, nullable=False)
    toxic_type = db.Column(db.String(20), nullable=False) # type of compound: antago, agonist, etc
    description = db.Column(db.String(200), nullable=False)
    canonical_smiles = db.Column(db.String(200), nullable=False)  # Column for canonical SMILES

if __name__ == '__main__':
    db.create_all()
# Create an instance of CompoundInfo for each entry in the dictionary
   
# Add the instance to the session
db.session.add(toxic)
# Commit the session to persist changes to the database
db.session.commit()