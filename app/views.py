"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
import time

from flask import render_template, request, jsonify

from app import app, db
from app.models import Myprofile
from forms import ProfileForm

    
###
# Routing for your application.
###
@app.route('/')
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
    profilelist = []
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        for item in profiles:
            profilelist.append('{username:'+ item.username + ' ,' + 'userid:' + str(item.id) + '}')
        return jsonify(users=profilelist)
    return render_template('profile_list.html',
                            profiles=profiles)

@app.route('/profile/<int:id>',methods=["POST","GET"])
def profile_view(id):
    profile = Myprofile.query.get(id)
    toret = []
    date = timeinfo()
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            toret.append('userid: ' + str(profile.id) + ', username: '
                         + profile.username + ', image: ' + profile.image + ', sex: ' + profile.sex + ', age: '
                         + str(profile.age))
            return jsonify(result=toret)
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
