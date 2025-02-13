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
