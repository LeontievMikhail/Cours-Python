from flask import Flask, url_for
import datetime
import platform

app = Flask(__name__)

@app.route('/')
def home():
   # return url_for('about')
   dat=str(datetime.datetime.now())+'<br><br>'+str(platform.win32_ver())
   # print(server)
   return f"<center><h1>Hello World<br><br>Now is %s</center><br><br>" % dat



@app.route('/about')
def about():
    return '<center>This is about page</center>'

if __name__=='__main__':
    app.run()
