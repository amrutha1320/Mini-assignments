const {MongoClient}=require('mongodb')
const mongourl='mongodb://127.0.0.1:27017'
const client=new MongoClient(mongourl);
const dbName='Ammu';
const express=require('express')
const url=require('url')
var api=express()
api.get('/',function(request,response){
    response.send("API server is online")
})
api.get('/message',async function(request,response){
    urldata=url.parse(request.url,true);
    var name=urldata.query.name;
    var rollno=urldata.query.rollno;
    console.log(name,rollno);

    await client.connect();
    console.log('connected to DB server');
    const db=client.db(dbName);
    const collection=db.collection('mss');
    const result=await collection.insertOne({"name":name,"rollno":rollno});
    response.send(result)
})
api.listen(2000,function(){
    console.log('API server is online,you can call APIs')
})