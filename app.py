from flask import Flask, render_template, redirect, url_for
# from config import DO THE CONFIG FILE
# from model import DO THE MODEL FILE
from forms import SignUpForm, LoginForm # forms for user input sign up, login, search bar
from api import get_compound_info, get_chembl_id_by_inchikey
from flask_bcrypt import bcrypt # password hashing
from flask_login import login_user, login_required, LoginManager, current_user # user authentication and session management

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

app = Flask(__name__)
# app.config.from_object(config[''])
# db.init_app(app) # initialize the database with the app (sets up the connection)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # type: ignore

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, (int(user_id)))


@app.route('/')
def home():
    return render_template('home.html') # generates the website from the template


@app.route('/login', methods=['GET', 'POST']) # GET is used when the user navigates to the login page, and POST is used when the user submits the login form.
def login():
    loginerror = None
    form = LoginForm()
    if form.validate_on_submit(): # check if the form has been submitted and if it's valid
        user = User.query.filter_by(email=form.email.data).first() # ask the db for user email
        if user: # if user exists check the password
            if (form_password := form.password.data):
                if bcrypt.checkpw(form_password.encode('utf8'), user.password): # hash the password to see if it matches the email
                    login_user(user) # log the user in
                    return redirect(url_for('userspace')) # redirect them to their userspace
        # if the user doesn't exist or the password is wrong, show an error message
        loginerror = "Invalid email or password."
    return render_template('auth/login.html', form=form, loginerror=loginerror) # get the user to the login page again


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


@app.route('/userspace', methods=['GET', 'POST']) # GET is used when the user navigates to the userspace page, and POST is used when the user submits the search form.
@login_required # the user must be logged in to access this view
def userspace(): # the user's personal space
    user = db.session.get(User, (int(current_user.id))) # get the user from the db
    form = UniprotForm() # create a new uniprot form
    if form.validate_on_submit(): # check if the form has been submitted and if it's valid
        seqanalysis = Seqanalysis.query.filter_by(uniprot=form.uniprot.data).first() # ask the db for the uniprot sequence
        if not seqanalysis: # if the sequence doesn't exist, get it from the uniprot api
            try: # try to get the uniprot info
                uniprot_info_tuple = get_unipro_info_tuple(form.uniprot.data) # get the uniprot info tuple
                seqanalysis = Seqanalysis(uniprot=uniprot_info_tuple[0], sequence=uniprot_info_tuple[1], mol_weight=uniprot_info_tuple[2]) # create a new sequence analysis with the uniprot info tuple
            except Exception as e: # if there's an error, print it
                print(e)
        if seqanalysis: # if the sequence exists, add it to the user's sequences
            user.sequences.append(seqanalysis) # add the sequence to the user's sequences
            db.session.add(user) # add the user to the db
            db.session.commit() # commit the user to the db
    # if the form is not valid, show the userspace page again
    return render_template('userspace.html', form=form, user_sequences=user.sequences)


@app.route('') # compound viewer space
@login_required
def compound_viewer():
    # compound_viewer = db.session.get
    # if compound_viewer in current_user.compounds:
        return render_template('compound_viewer.html')
    # else:
        return redirect(url_for('userspace'))

hostedApp = Flask(__name__)
# hostedApp.config.from_object('config')
# hostedApp.wsgi_app = DispatcherMiddleware(NotFound(), {f"PREFIX": app})

if __name__ == '__main__':
    hostedApp.run(debug=True) # run the app in debug mode, switch off to publish