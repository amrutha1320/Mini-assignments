


from flask import Flask,render_template,request,redirect,session
from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
db=client['Ammu']
c=db['flaskapp']
app=Flask(__name__)
app.secret_key='Ammu'
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')
@app.route('/dashboard')
def dashboardpage():
    owner=session['username']
    return render_template('dashboard.html',owner=owner)
@app.route('/insertnotes')
def insertnotespage():
    return render_template('insertnotes.html')
@app.route('/viewnotes')
def viewnotes():
    c1=db['notes']
    data=[]
    for i in c1.find():
        if i['owner']==session['username']:
            data.append(i['notes'])
    return render_template('viewnotes.html',data=data,l=len(data))
@app.route('/formdata',methods=['post'])
def formdata():
    name=request.form['name']
    email=request.form['email']
    mobile=request.form['mobile']
    password=request.form['password']
    print(name,email,mobile,password)
    for i in c.find():
        if i['mobile']==mobile:
           return render_template('index.html',err='you have already registered')
    k={}
    k['name']=name
    k['email']=email
    k['mobile']=mobile
    k['password']=password
    c.insert_one(k)
    return render_template('index.html',res='you have registered successfully')
@app.route('/logindata',methods=['post'])
def logindata():
    mobile=request.form['mobile']
    password=request.form['password']
    print(mobile,password)
    for i in c.find():
        if i['mobile']==mobile and i['password']==password:
            session['username']=mobile
            return redirect('/dashboard')
           # return render_template('login.html',res1='valid credentials')
        
    return render_template('login.html',err1='invalid credentials')

@app.route('/logout')
def logout():
    session['username']=None
    return redirect('/')

@app.route('/insertnotesdata',methods=['post'])
def insertnotesdata():
    notes=request.form['notes']
    owner=session['username']
    print(notes,owner)
    c1=db['notes']
    k={}
    k['owner']=owner
    k['notes']=notes
    c1.insert_one(k)

    return render_template('insertnotes.html',res2='Notes saved')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)

