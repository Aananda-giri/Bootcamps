# Book : Beginning node js

- [source-code](github.com/greglim81/expresss_chap3-8)

Nodejs, Express, MongoDB

- user auth, data validation, async js, password hashing, Express, mongo, template engine, maintaining user session
- log out, new post

## What is nodejs?

- client makes a resqueest and server responds with html
- server side languages: node, php, ruby, python,...
- MEAN stack: mongo, express, Angular, Node
- MERN stack: use react as front end instead of angular

node -v
npm -v
pnpm -v

## Creating our first server

- we call the function request handler

# Chapter 2

## express js

- got to `npmjs.com` and search for express
- package.json to track all package and their versions used in our app.
- `npm install express`
  or
  `npm install pnpm`
  `pnpm install express`
- `npm init` : generates package.json for us

```
const express=require('express');   // require express module
const app = express();   // calls express function to start new Express app

app.listen(3000, () =>{
    console.log("Ap listening on port 3000");
})
```

`node index.js`

# Chapter 3

- use nodemon on dev to auto detect changes
- blog template from [startbootstrap](https://startbootstrap.com/theme/clean-blog)
- Add "scripts to package.json" and use `pnpm start` to run the code.

# chapter 4

- use ejs for template engine
- reusable template layouts: header, footer, navbar, scripts

# Chapter 5

- mongodb
- mongodb compass
- CRUD: Create, Read, Update, Delete

# Chapter 6

- data from mongo: post, date
- [ ] make search function work

# Chapter 7: image file upload

- use
- `enctype="multipart/form-data"` in form tells browser form contains multimedia data

# Chapter 8: Express Middlewares

- middlewares are functions express executes in the middle after request which produce output that can be final output or be used by next middleware.
- // "Custom middleware called" will be displayed every time you refresh the app.

// apply this middleware for specific url pattern (specific request).
app.use('posts/store', validateMiddleWare);

```

- Good use case: form validation
```

# Chapter 9: Refactoring to MVC

- Model view controller
  Model: structure of the data
  View: what is presented to the user (e.g. ejs files)
  Controller: controls requests of user and genereate appropriate response

- user interacts with view, which genereates appropriate request which is handele by controlller which then renders the appropriate view with Model data as response.

- in this chapter, we will refactor controller layer
- `controllers/newPost.js`

# Chapter 10: User Reginsration

- user interacts with view, which genereates appropriate request which is handele by controlller which then renders the appropriate view with Model data as response.

## encrypt the password

- mongoose model hook (hook is just a middleware)
- `npm i bcrypt --save` to encrypt passwords
- [ ] todo: error: bcrypt MODULE_NOT_FOUND
