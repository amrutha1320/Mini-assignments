from flask import Flask,request
from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
db=client['Ammu']
collection=db['mss']
api=Flask(__name__)
@api.route('/')
def home():
    return ('API server is online,you can call APIs')
@api.route('/message',methods=['GET'])
def message():
    name=request.args.get('name')
    rollno=request.args.get('rollno')
    print(name,rollno)
    k={}
    k['name']=name
    k['rollno']=rollno
    collection.insert_one(k)
    return ('succesfully inserted into mongodb')
if(__name__)=="__main__":
    api.run(host='0.0.0.0',port=5001,debug=True)