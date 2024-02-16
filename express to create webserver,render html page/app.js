const express=require('express')
const fs=require('fs')
var app=express();
app.get('/',function(request,response){
    fs.readFile('index.html',function(err,data){
        if(err)throw err;
        response.end(data);
    })
})
app.listen(2000,function(){
    console.log('server started');
})