const express=require('express');
var app=express()
app.get('/',function(request,response){
    response.send("hi ammu");
})

app.get('/ammu',function(request,response){
    response.send("you are in express");
})
app.listen(2000,function(){
    console.log('server started');
})