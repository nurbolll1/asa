from flask import Flask,render_template,url_for,request,redirect
from db import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/Notification')
def Notification():
    datas = session.query(Notification_db).all()

    if datas:
        print(datas)
        return render_template('notification.html', datas = datas)
    else:
      return render_template('notification.html')  

@app.route("/Add-Notification", methods = ['post','get'])
def Add_Notification():
    if request.method == 'POST':
        img = request.form.get('image_url')
        text = request.form.get('text')
        new_notification = Notification_db(url_img=img, text=text)
        session.add(new_notification)
        session.commit()
        return redirect(url_for('Notification'))
    else:
        return render_template('add_notification.html')

@app.route("/Information")
def Information():
    return render_template("information.html")

@app.route("/Cky")
def cky():
    return render_template("cky.html")

app.run(debug=False, host = '127.0.0.1', port='8080')

session.close()

