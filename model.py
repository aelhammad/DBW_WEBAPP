from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from api import pubchem_requests, get_compound_data, get_ghs_pictograms, query_dictionary
import json
from sqlalchemy import text

#compounds = ['Benzene', 'Chloroform', 'Dieldrin', 'Benzidine', 'Heptachlor']

compounds = query_dictionary.keys()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dbwapp:toxicdb33@localhost/toxbrowser'  # Update with your database URI
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

entry_pictogram_association = db.Table(
    'entry_pictogram_association',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
    db.Column('pictogram_id', db.Integer, db.ForeignKey('pictograms.id'))
)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    pubchem_id = db.Column(db.String(20), nullable=False)
    chembl_id = db.Column(db.String(20), nullable=False)
    inchi_key = db.Column(db.String(30), nullable=False)
    chemical_formula = db.Column(db.String(50), nullable=False)
    compound_name = db.Column(db.Text, nullable=False)
    molecular_weight = db.Column(db.Float)
    description = db.Column(db.Text)
    description1 = db.Column(db.Text)
    canonical_smiles = db.Column(db.Text)
    isomeric_smiles = db.Column(db.Text)
    mechanism_of_toxicity = db.Column(db.Text)
    treatment = db.Column(db.Text)
    year_id = db.Column(db.Integer, db.ForeignKey('year.id'))
    year = db.relationship('Year', back_populates='entries_rel')
    pictograms = db.relationship('Pictograms', secondary=entry_pictogram_association, backref='entries')
    type_names = db.relationship('TypeName', secondary='entry_type_names_association', backref='entries')


class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_year = db.Column(db.Integer)
    entries_rel = db.relationship('Entry', back_populates='year', foreign_keys='Entry.year_id')

class Health_effects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    health_effects = db.Column(db.Text)

class Pictograms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pictogram_url = db.Column(db.Text)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id', ondelete='CASCADE'))

entry_type_names_association = db.Table('entry_type_names_association',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
    db.Column('type_name_id', db.Integer, db.ForeignKey('type_name.id'))
)

class TypeName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), unique=True)


if __name__ == '__main__':
    with app.app_context():
        
        # Drop all tables
        db.drop_all()

        # Create all tables
        db.create_all()

        # Keep track of years already added
        added_years = set()

        # Iterate over the compounds
        for compound in compounds:
            compound_data = get_compound_data(query_dictionary, compound)
            cid = query_dictionary[compound][0]
            compound_info = pubchem_requests(cid)
            pictogram_urls = get_ghs_pictograms(cid)

            pubchem_id, chembl_id, type_names, mechanism_of_toxicity, description1, toxicity, symptoms, treatment, health_effects = compound_data

            compound_name, chemical_formula, canonical_smiles, isomeric_smiles, molecular_weight, inchi_key, description, creation_year = compound_info


            # Check if the year already exists in the Year table
            year_obj = Year.query.filter_by(creation_year=creation_year).first()

            if not year_obj:
                # If the year doesn't exist, add it to the Year table
                year_obj = Year(creation_year=creation_year)
                db.session.add(year_obj)
                db.session.commit()

            # Create Entry object
            entry = Entry(
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
                treatment=treatment,
                year_id=year_obj.id
            )

            # Add Entry object to the session
            db.session.add(entry)
            db.session.commit()

            # Insert data into Health_effects, Pictograms, and TypeNames
            health_effect = Health_effects(entry_id=entry.id, health_effects=health_effects)
            db.session.add(health_effect)

            if pictogram_urls:
                for url in set(pictogram_urls):
                    pictogram = Pictograms.query.filter_by(pictogram_url=url).first()
                    if not pictogram:
                        pictogram = Pictograms(pictogram_url=url)
                        db.session.add(pictogram)
                        db.session.commit()
                    entry.pictograms.append(pictogram)
            if type_names:
                for type_name in type_names:
                    type_name_obj = TypeName.query.filter_by(type_name=type_name).first()
                    if not type_name_obj:
                        type_name_obj = TypeName(type_name=type_name)
                        db.session.add(type_name_obj)
                    # Associate TypeName object with Entry object
                    entry.type_names.append(type_name_obj)

# Commit changes to the TypeNames table
            db.session.commit()




'''
To acess the pictograms use: 

# Assuming you have an `entry_id` for the entry you want to query
entry = Entry.query.get(entry_id)

# Access the pictograms associated with the entry
associated_pictograms = entry.pictograms

# Now you can iterate over the associated_pictograms list to get their details
for pictogram in associated_pictograms:
    print(pictogram.pictogram_url)

or in MYSQL:

SELECT p.pictogram_url
FROM entry e
JOIN entry_pictogram_association epa ON e.id = epa.entry_id
JOIN pictograms p ON epa.pictogram_id = p.id
WHERE e.id = 1;


'''