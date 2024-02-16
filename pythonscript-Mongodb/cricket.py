from pymongo import MongoClient # pymongo - module, MongoClient - Class
try:
    client=MongoClient('127.0.0.1',27017) # ip address, port number 
    print('MongoDB Server Connected')
    db=client['Cricket_Details']
    collection=db['Cricket_team']
    print("Enter no. of players in the team:")
    n=int(input())
    for i in range(1,n+1):
        print("Enter player",i,"details")
        Player_name=input("Enter player name:")
        Player_team=input("Enter player team:")      
        Player_role=input("Enter Player role:")                                     
        k={}
        k['Player_name']=Player_name
        k['Player_team']=Player_team
        k['Player_role']=Player_role
        collection.insert_one(k)
    print("The cricket team details are:")
    for i in collection.find():
        print(i)
except:
    print("Mongodb server not connected")