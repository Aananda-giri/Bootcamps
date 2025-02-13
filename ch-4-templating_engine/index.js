const express = require('express');
const path=require('path');

const app = new express();

app.use(express.static('public'))


// set ejs as our templating engine that any files ending with .ejs should be rendered with EJS package.
// rename index.html to index.ejs
const ejs = require('ejs');
app.set('view engine','ejs');

app.listen(4000,() => {
   console.log('App listening on port 4000') 
});


app.get('/', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    res.render('index');
})

app.get('/about', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    res.render('about');
})

app.get('/contact', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/contact.html'))
    res.render('contact');
})

app.get('/post', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/post.html'))
    res.render('post');
})