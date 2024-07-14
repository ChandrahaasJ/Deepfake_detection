const express=require('express');
const app=express();
const multer=require('multer');


app.get('/home',(req,res)=>{
    res.send("JI");
})

app.post('/video',(req,res)=>{


})


app.post('/image',(req,res)=>{
    
})

app.listen(10)