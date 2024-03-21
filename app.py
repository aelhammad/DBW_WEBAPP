from flask import Flask, render_template, redirect, url_for, request
from config import config, PREFIX
from forms import SignUpForm, LoginForm, ToxicForm
from api import get_compound_data
from flask_bcrypt import bcrypt # password hashing
from flask_login import login_user, login_required, LoginManager, current_user # user authentication and session management
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from model import User, Userdata, Entry, Health_effects, Year, Pictograms, TypeName,db
from flask import jsonify
import logging


app = Flask(__name__)
app.config.from_object(config['production'])
db.init_app(app) # initialize the database with the app (sets up the connection)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # type: ignore

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, (int(user_id)))


@app.route('/')
def home():
    return render_template('home.html') # generates the website from the template
@app.route('/about')
def about():
    return render_template('about_us.html') # generates the website from the template
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/guide')
def guide():
    return render_template('user_guide.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginerror = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            logging.info(f"Retrieved hashed password: {user.password}")
            logging.info(f"Form password before encoding: {form.password.data}")
            entered_password = form.password.data.encode('utf-8')  # Get the raw password from the form
            if bcrypt.checkpw(entered_password, user.password.encode('utf-8')):  # Encode the hashed password from the database
                login_user(user)
                return redirect(url_for('userspace'))
            else:
                logging.error("Password comparison failed.")
                loginerror = "Invalid email or password."
        else:
            logging.error("User not found.")
            loginerror = "Invalid email or password."
    return render_template('auth/login.html', form=form, loginerror=loginerror)




@app.route('/signup', methods=['GET', 'POST']) # GET is used when the user navigates to the signup page, and POST is used when the user submits the signup form.
def signup():
    form = SignUpForm()
    if form.validate_on_submit(): # check if the form has been submitted and if it's valid
        if (form_password := form.password.data): # check if the password is not empty
            hashed_password = bcrypt.hashpw(form_password.encode('utf8'), bcrypt.gensalt()) # hash the password
            new_user = User(email=form.email.data, password=hashed_password) # create a new user with the email and hashed password
            db.session.add(new_user) # add the new user to the db
            db.session.flush() # commit the new user to the db
            db.session.refresh(new_user) # refresh the db session
            new_user_data = Userdata(name=form.name.data, surname=form.surname.data,
                                     institution=form.institution.data, user_id=new_user.id) # create a new user data with the user id
            db.session.add(new_user_data) # add the new user data to the db
            db.session.commit() # commit the new user data to the db
            return redirect(url_for('userspace')) # redirect the user to their userspace
    # if the form is not valid or the user already exists, show the signup page again
    return render_template('auth/signup.html', form=form)


@app.route('/get_toxic', methods=['GET'])
def get_toxic():
    # Get the search query from the request query string
    search_query = request.args.get('search_query')
    
    compound = None
    
    # Perform the search based on the provided query
    if search_query:
        # Fetch compound information from the database based on the provided query
        compound = Entry.query.filter(
            (Entry.compound_name == search_query) | 
            (Entry.id == search_query) |
            (Entry.inchi_key == search_query)
        ).first()
    
    if compound:
        # If compound exists, render the template with compound information
        return render_template('get_toxic.html', compound=compound)
    
    # If compound is not found, display an error message or redirect to another page
    return render_template('not_found.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    term = request.args.get('term')
    # Query the database for compound names that start with the user's input
    matching_compounds = Entry.query.filter(Entry.compound_name.startswith(term)).all()
    # Extract the compound names from the query results
    suggestions = [compound.compound_name for compound in matching_compounds]
    return jsonify(suggestions)

 
@app.route('/compound_types')
def compound_types():
    compound_types = TypeName.query.all()
    return render_template('home.html', compound_types=compound_types)

@app.route('/filtered_compounds/<int:type_id>')
def filtered_compounds(type_id):
    # Query the database for compounds with the specified type ID
    compounds = Entry.query.filter_by(type_id=type_id).all()
    return render_template('advanced.html', compounds=compounds)

@app.route('/filtered_compounds_by_pictogram/<int:pictogram_id>')
def filtered_compounds_by_pictogram(pictogram_id):
    pictogram = Pictograms.query.get(pictogram_id)
    if pictogram:
        compounds = Entry.query.filter(Entry.pictograms.any(id=pictogram_id)).all()
        return render_template('advanced.html', compounds=compounds)


@app.route('/userspace', methods=['GET', 'POST']) 
def userspace():
    # user = db.session.get(User, (int(current_user.id)))
    form = ToxicForm()
    if form.validate_on_submit():
        toxicentry = Entry.query.filter_by(toxic=form.toxic.data).first() # ask the db for the uniprot sequence
        if not toxicentry: # if the sequence doesn't exist, get it from the uniprot api
            try: # try to get the uniprot info
                compound_dictionary = get_compound_data(form.toxic.data) # get the uniprot info tuple
                toxicentry = Entry(toxic=compound_dictionary.items()) # create a new sequence analysis with the uniprot info tuple
            except Exception as e: # if there's an error, print it
                print(e)
        # if toxicentry: # if the sequence exists, add it to the user's sequences
            # user.sequences.append(toxicentry) add the sequence to the user's sequences
            # db.session.add(user) # add the user to the db
            # db.session.commit() # commit the user to the db
    # if the form is not valid, show the userspace page again
    return render_template('userspace.html', form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('home'))
    # return render_template('home.html')


''' 
@app.route('') # compound viewer space
@login_required
def compound_viewer():
    # compound_viewer = db.session.get
    # if compound_viewer in current_user.compounds:
        return render_template('compound_viewer.html')
    # else:
        return redirect(url_for('userspace'))
'''
hostedApp = Flask(__name__)
# hostedApp.config.from_object('config')
# hostedApp.wsgi_app = DispatcherMiddleware(NotFound(), {f"PREFIX": app})

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode, switch off to publish