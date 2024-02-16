# Connect with MongoDB

from pymongo import MongoClient # pymongo - module, MongoClient - Class
try:
    client=MongoClient('127.0.0.1',27017) # ip address, port number 
    print('MongoDB Server Connected')
    db=client['Amrutha']
    collection=db['mss']
    print("The initial collection data:")
    for i in collection.find():
        print(i)
     # insert data
    print("Inserting data into collection:")
    name=input("Enter name:")
    rollno=input("Enter rollno:")                                           
    k={}
    k['name']=name
    k['rollno']=rollno
    collection.insert_one(k)
    for i in collection.find():
        pass
    else:
        print(i) 
    print("Creating a query")
    #creating query 
    query={'name':'abi'}
    for i in collection.find(query):
        print(i)

    #updating a document
    print("Updating a document")
    query={'name':'kohli'}
    newvalue={"$set":{'name':'pinky'}}
    collection.update_one(query,newvalue)

    #deleting the document
    print("Deleting a document")
    
    query={'name':'abi'}
    collection.delete_one(query)
    print("The final collection after all the Crud operations:")
    for i in collection.find():
        print(i)

except:
    print('MongoDB connection Failed')