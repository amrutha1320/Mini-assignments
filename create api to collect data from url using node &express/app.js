const express=require('express');
const url=require('url');
var api=express()
api.get('/',function(request,response){
    response.send("API server is online")
})
api.get('/data',function(request,response){
    urldata=url.parse(request.url,true);
    var name=urldata.query.name;
    var rollno=urldata.query.rollno;
    var number=urldata.query.number;
    var college=urldata.query.college;
    var password=urldata.query.password;

    
    response.json({Rollno:rollno,name:name,number:number,college:college,password:password});
})
api.listen(2000,function(){
    console.log('API server is online,you can call APIs')
})

