var client=require('mongodb').Mongoclient;
var url="mongodb://127.0.0.1:27017/Ammu";
client.connect(url,function(err,db){
    if(err){
        throw err;

    }
    console.log('Database connected');
});