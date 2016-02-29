"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import time,os

from werkzeug.utils import secure_filename

from flask import render_template, request, redirect, url_for,jsonify,g,session

from app.models import Myprofile

from app import app, db
from app import oid

from flask.ext.login import login_user,current_user,login_required
from flask.ext.login import LoginManager

from forms import ProfileForm, LoginForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
    return Myprofile.query.get(userid)


@app.before_request
def before_request():
    g.user = current_user
    
###
# Routing for your application.
###
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    print app.config['OPENID_PROVIDERS']
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
def login_validate():
    form = LoginForm()
    if request.method == "POST":
        pass
    # change this to actually validate the user
    if form.username.data:
        # login and validate the user...

        # missing
        # based on password and username
        # get user id, load into session
        user = load_user("1")
        login_user(user)
        #flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("home"))
    return render_template("login.html", form=form)

@app.route('/')
@login_required
def home():
    """Render website's home page."""
    return render_template('home.html')

  
@app.route('/profile', methods=['POST','GET'])
def profile_add():
    form = ProfileForm()
    if request.method == 'POST' and form.validate():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        file = request.files['image']
        filename = file.filename
        file.save(os.path.join('app/static/uploads', filename))

        username = request.form['username']
        sex = request.form['sex']

        # write the information to the database
        newprofile = Myprofile(first_name=first_name,
                               last_name=last_name,
                               age=age,
                               sex=sex,
                               username=username,
                               image='/static/uploads/'+filename)
        db.session.add(newprofile)
        db.session.commit()

        return "{} {} was added to the database".format(request.form['first_name'],
                                             request.form['last_name'])
    return render_template('profile_add.html',
                           form=form)

@app.route('/profiles/',methods=["POST","GET"])
def profile_list():
    profiles = Myprofile.query.all()
    if request.method == "GET":
        return jsonify(username=str(profiles[1]))
    return render_template('profile_list.html',
                            profiles=profiles)

@app.route('/profile/<int:id>',methods=["POST","GET"])
def profile_view(id):
    profile = Myprofile.query.get(id)
    date = timeinfo()
    return render_template('profile_view.html',profile=profile,date=date)

def timeinfo():
    """Render the current date"""
    date ='Profile added on:' + " " + time.strftime("%a, %b %d %Y")
    return date

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
