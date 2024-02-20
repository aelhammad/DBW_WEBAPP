from flask import Flask, render_template, redirect, url_for
from config import config, PREFIX
from forms import SignUpForm, LoginForm, ToxicForm
from api import get_compound_data
from flask_bcrypt import bcrypt # password hashing
from flask_login import login_user, login_required, LoginManager, current_user # user authentication and session management
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from model import User, Userdata, Entry, Health_effects, Year, Pictograms, TypeName,db


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


@app.route('/get_toxic/<int:compound_id>')
def compound_details(compound_id):
    # Busca la entrada correspondiente al ID del compuesto
    compound = Entry.query.get(compound_id)
    if compound:
        return render_template('get_toxic.html', compound=compound)
    else:
        return "Compuesto no encontrado", 404  # Devuelve un error 404 si el compuesto no se encuentra



 
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