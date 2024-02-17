from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from api import pubchem_requests, get_compound_data, get_ghs_pictograms,query_dictionary



compound_data = get_compound_data(query_dictionary, 'Benzene')
cid = query_dictionary['Benzene'][0]
compound_info = pubchem_requests(cid)
pictogram_urls = get_ghs_pictograms(cid)

if compound_data:
    pubchem_id, chembl_id, type_names, mechanism_of_toxicity, description1, toxicity, symptoms, treatment, health_effects = compound_data

if compound_info is not None:
    compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description, creation_year = compound_info


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://toxicbrowser'  # Update with your database URI
db = SQLAlchemy(app)

user_entries = db.Table('user_entries',
                        db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                        )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_data = db.relationship('Userdata', backref='user')
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
    inchi_key = db.Column(db.String(30), nullable=False)
    chemical_formula = db.Column(db.String, nullable=False) # from pubchem
    compound_name = db.Column(db.String(50), nullable=False) # from pubchem
    molecular_weight = db.Column(db.Float) # from pubchem
    type_names = db.Column(db.String(40)) # type of compound: antago, agonist, etc
    description = db.Column(db.String(lenght=None)) # from json and pubchem
    description1 = db.Column(db.String(lenght = None)) # from json and pubchem
    canonical_smiles = db.Column(db.String(200))  # Column for canonical SMILES, pubchem
    isomeric_smiles = db.Column(db.String(200))  # Column for isomeric SMILES, pubchem 
    mechanism_of_toxicity = db.Column(db.String(200))  # from td3
    treatment = db.Column(db.String(200))  # from td3

class Health_effects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    health_effects = db.Column(db.String(200))

class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    creation_year = db.Column(db.Integer, nullable=False)
    entries = db.relationship('Entry', backref='year')

if __name__ == '__main__':
    db.create_all()
    # Add your code to create and commit instances to the session here
    db.session.commit()