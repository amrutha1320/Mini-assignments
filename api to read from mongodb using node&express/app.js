const express=require('express');
const url=require('url')
const {MongoClient}=require('mongodb')
const mongourl='mongodb://127.0.0.1:27017'
const client=new MongoClient(mongourl);
const dbName='Ammu';
var api=express();
api.get('/',function(request,response){
    response.send('api server in online');
})
api.get('/data',async function(request,response){
    await client.connect();
    console.log("server connected");
    const db=client.db(dbName);
    const collection=db.collection('mss');
    const result=await collection.find({}).toArray();  
    for(let item of result){
        console.log(item);

    }                                       
    response.send(result);
})
api.listen(2000,function(){
    console.log('API server is started');
})    
