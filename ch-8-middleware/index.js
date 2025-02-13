const express = require('express');
const path=require('path');
const mongoose = require('mongoose');

const fileUpload =require("express-fileupload");

const bodyParser = require('body-parser');
const BlogPost = require('./models/BlogPost');

const app = new express();

// index.js
const customMiddleWare = (req, res, next) => {
    console.log("Custom middleware called");
    next()
}
app.use(customMiddleWare)

app.use(express.static('public'))

// middleware to parse post requests
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}))

app.use(fileUpload());


// set ejs as our templating engine that any files ending with .ejs should be rendered with EJS package.
// rename index.html to index.ejs
const ejs = require('ejs');
app.set('view engine','ejs');

// connect to local mongo database
// Connect to MongoDB first
mongoose.connect('mongodb://localhost:27017/my_database', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('Connected to MongoDB');
})
.catch(error => {
    console.error('MongoDB connection error:', error);
});



app.listen(4000,() => {
   console.log('App listening on port 4000') 
});


app.get('/', async (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    const blogposts = await BlogPost.find({});
    res.render('index', {
        // blogposts: blogposts
        blogposts
    });
})

app.get('/about', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    res.render('about');
})

app.get('/contact', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/contact.html'))
    res.render('contact');
})

app.get('/post/:id', async (req,res)=>{
    const blogpost = await BlogPost.findById(req.params.id);
    // res.sendFile(path.resolve(__dirname, 'pages/post.html'))
    res.render('post', {
        blogpost
    });
})

// to create new post
app.get('/posts/new', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/post.html'))
    res.render('create');
})


// todo: get the images storage working
app.post('/posts/store', async (req, res) => {
    // let image = req.files.image;
    // image.mv(path.resolve(__dirname, 'public/img', image.name)), async (error)=>{
    // }

    console.log(req.body);
    // req.body contains data in format: {"title":"some-title", "body": "some-body"}
    try {
        await BlogPost.create({...req.body, image:'/img/' + image.name});
        res.redirect('/');
    } catch (error) {
        console.error('Error saving post:', error);
        res.redirect('/posts/new');
    }
});

// todo: get it working
// to create new post
app.get('/search', async (req,res)=>{
    
    console.log('called search')
    console.log(req.body);

    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    // const blogposts = await BlogPost.find({});
    
    //
    const query = req.params.query;
    
    // query in title
    const blogposts = await BlogPost.find({
        title:/query/
    });
    res.render('index', {
        // blogposts: blogposts
        blogposts
    });
})





// custom form validation middlewawre
const validateMiddleWare = (req, res, next) =>{
    if(req.files ==null || req.body.title == null || req.body.title ==null){
        return res.redirect('posts/new');   // Redirect back to create post page
    }
    next()
}

// apply this middleware for specific request (specific request).
app.use('posts/store', validateMiddleWare);