const express = require('express');
// const path=require('path');
const mongoose = require('mongoose');
require('dotenv').config();

const fileUpload =require("express-fileupload");

const bodyParser = require('body-parser');
// const BlogPost = require('./models/BlogPost');

const app = new express();

const expressSession = require('express-session')

app.use(expressSession({
  secret:'keyboard cat' // secret string is used by express-session package to sign and encrypt this sessionID secret string
}))

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

const authMiddleware = require('./middleware/authMiddleware');
const redirectIfAuthenticatedMiddleware = require('./middleware/redirectIfAuthenticatedMiddleware');

// set ejs as our templating engine that any files ending with .ejs should be rendered with EJS package.
// rename index.html to index.ejs
const ejs = require('ejs');
app.set('view engine','ejs');

// flush error data once at the end of current request (after being shown once).
const flash = require('connect-flash');
app.use(flash());

// connect to local mongo database
// Connect to MongoDB first

// use mongo uri from .env file if available
let mongo_uri = process.env.mongo_uri;
if (!mongo_uri){mongo_uri='mongodb://localhost:27017/my_database'}
mongoose.connect(mongo_uri, {
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


// app.get('/', async (req,res)=>{
//     // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
//     const blogposts = await BlogPost.find({});
//     res.render('index', {
//         // blogposts: blogposts
//         blogposts
//     });
// })

app.get('/about', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/about.html'))
    res.render('about');
})

app.get('/contact', (req,res)=>{
    // res.sendFile(path.resolve(__dirname, 'pages/contact.html'))
    res.render('contact');
})

// app.get('/post/:id', async (req,res)=>{
//     const blogpost = await BlogPost.findById(req.params.id);
//     // res.sendFile(path.resolve(__dirname, 'pages/post.html'))
//     res.render('post', {
//         blogpost
//     });
// })

// to conditionally display login/logout/register buttons
// -------------------------------------------------------
global.loggedIn = null; // declare global variable (accessible from all .ejs files)

app.use("*", (req, res, next) => {
    // This middleware should be executed in all requests 
    
    loggedIn = req.session.userId;  //
    console.log(`loggedIn: ${loggedIn}`);
    next();
})


const newPostController = require('./controllers/newPost');
const homeController = require('./controllers/home');
const getPostController = require('./controllers/getPost');
const storePostController = require('./controllers/storePost');
const newUserController = require('./controllers/newUser');
const storeUserController = require('./controllers/storeUser');
const loginController = require('./controllers/login');
const loginUserController = require('./controllers/loginUser');
const logoutController = require('./controllers/logout');

app.get('/', homeController);
app.get('/post/:id', getPostController);
app.post('/posts/store', authMiddleware, storePostController);
app.get('/posts/new', authMiddleware, newPostController);   // auth middleware before creating new post.
app.get('/auth/register', redirectIfAuthenticatedMiddleware, newUserController);
app.post('/users/register', redirectIfAuthenticatedMiddleware, storeUserController);
app.get('/auth/login', redirectIfAuthenticatedMiddleware, loginController);
app.post('/users/login', redirectIfAuthenticatedMiddleware, loginUserController);   // apply login user controller
app.get('/auth/logout', logoutController);
app.use((req, res)=>{res.render('notfound');}) // 404 page


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



const validateMiddleWare = require("./middleware/validationMiddleware");

// apply this middleware for specific request (specific request).
app.use('posts/store', validateMiddleWare);