from flask import Flask, request, render_template
import pyrebase
import datetime

config = {
  "apiKey": "AIzaSyANS18NvbjWWwx1JgRxAdWu4CmZzEdVtxM",
  "authDomain": "attendancee-d816b.firebaseapp.com",
  "databaseURL": "https://attendancee-d816b-default-rtdb.firebaseio.com/",
  "storageBucket": "attendancee-d816b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)




@app.route('/',methods=['POST','GET'])   
def result():
    if request.method =='POST':
        if request.form['submit'] == 'submit':
             x = datetime.datetime.now()
             x = x.strftime("%Y-%m-%d %H:%M:%S")
             
             name = request.form.get('name')
             contact = request.form.get('cn')
             roll = request.form.get('rn')
             university = request.form.get('un')
             
             print(name,contact,roll,university)

             payload = {'time' : x, 'Name' : name, 'ContactNo' : contact, 'RollNo' : roll, 'UniversityNo' : university}

             db.child('attendancebot').push(payload) 

             return render_template('indexx.html',submit = True,name = payload['Name'])
    return render_template('indexx.html', submit = False)

if __name__ == "__main__":
    app.run(debug = True)