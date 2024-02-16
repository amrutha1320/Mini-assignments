from flask import Flask,request
api=Flask(__name__)
@api.route('/')
def home():
    return ('API server is online,you can call APIs')
@api.route('/message',methods=['GET'])
def message():
    name=request.args.get('name')
    rollno=request.args.get('rollno')
    print(name,rollno)
    return('Name is {0},Roll no is {1}'.format(name,rollno))
if(__name__)=="__main__":
    api.run(host='0.0.0.0',port=5001,debug=True)