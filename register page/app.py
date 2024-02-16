from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/formdata',methods=['post'])
def formdata():
    name=request.form['name']
    email=request.form['email']
    mobile=request.form['mobile']
    passsword=request.form['password']
    print(name,email,mobile,passsword)
    return render_template('index.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
