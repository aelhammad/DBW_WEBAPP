from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from api import pubchem_requests, get_compound_data, get_ghs_pictograms,query_dictionary
import json



compound_data = get_compound_data(query_dictionary, 'Benzene')
cid = query_dictionary['Benzene'][0]
compound_info = pubchem_requests(cid)
pictogram_urls = get_ghs_pictograms(cid)

pubchem_id, chembl_id, type_names, mechanism_of_toxicity, description1, toxicity, symptoms, treatment, health_effects = compound_data


compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description, creation_year = compound_info

type_names = json.dumps(type_names)
pictogram_urls = json.dumps(pictogram_urls)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toxicbrowser.db'  # Update with your database URI
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
    chemical_formula = db.Column(db.String, nullable=False)
    compound_name = db.Column(db.String(50), nullable=False)
    molecular_weight = db.Column(db.Float)
    description = db.Column(db.String(length=None))
    description1 = db.Column(db.String(length=None))
    canonical_smiles = db.Column(db.String(200))
    isomeric_smiles = db.Column(db.String(200))
    mechanism_of_toxicity = db.Column(db.String(200))
    treatment = db.Column(db.String(200))
    year_id = db.Column(db.Integer, db.ForeignKey('year.id'))  # Foreign key reference to Year table
    year = db.relationship('Year', backref='entry')  # Relationship with Year table
    pictograms = db.relationship('Pictograms', backref='entry')
    typename = db.relationship('TypeName', backref='entry')



class Health_effects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    health_effects = db.Column(db.String(200))

class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_year = db.Column(db.Integer)


class Pictograms(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    pictogram_urls = db.Column(db.String(200))

class TypeName(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    type_names = db.Column(db.String(200))
    

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        benzene_entry = Entry(
            id = 1,
            pubchem_id=pubchem_id,
            chembl_id=chembl_id,
            inchi_key=inchi_key,
            chemical_formula=chemical_formula,
            compound_name=compound_name,
            molecular_weight=molecular_weight,
            description=description,
            description1=description1,
            canonical_smiles=canonical_smiles,
            isomeric_smiles=isomeric_smiles,
            mechanism_of_toxicity=mechanism_of_toxicity,
            treatment=treatment
        )
        db.session.add(benzene_entry)

        benzene_year = Year(creation_year=creation_year)
        db.session.add(benzene_year)

        benzene_health_effects = Health_effects(entry_id=benzene_entry.id, health_effects=health_effects)
        db.session.add(benzene_health_effects)

        benzene_pictograms = Pictograms(entry_id=benzene_entry.id, pictogram_urls=pictogram_urls)
        db.session.add(benzene_pictograms)

        benzene_type_names = TypeName(entry_id=benzene_entry.id, type_names=type_names)
        db.session.add(benzene_type_names)



        db.session.commit()