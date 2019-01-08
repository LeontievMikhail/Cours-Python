### pip install flask
### pip install
### pip install flask-mysqldb
### pip install flask-WTF
### pip install passlib
###


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt



app = Flask(__name__)

#confi MySQL
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_PORT']= 3306
mysql.init_app(app)
#init MYSQL


Articles=Articles()

@app.route('/')
def index():
    return  render_template('home.html')

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/articles')
def articles():
    return  render_template('articles.html', articles=Articles )


@app.route('/article/<string:id>')
def article(id):
    return  render_template('article.html', id=id )

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username=StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not math')
    ])
    confirm=PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name= form.name.data
        email= form.email.data
        username=form.username.data
        password=sha256_crypt.encrypt(str(form.password.data))
        #Create cursor
        cur= mysql.connection.cursor()
        #executy query
        sql=("INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)")
        sql1=(name, email, username, password)
        cur.execute(sql, sql1)
        #commit to DB
        mysql.connection.commit()

        #close connection
        # cur.close()

        flash('You are now registered and can log in', 'success')



        return redirect(url_for('register'))

    return render_template('register.html', form=form)

if __name__=="__main__":
    app.secret_key='secret123'
    app.run(debug=True)

