# Chapter 10: User Reginsration

- Model view controller
  Model: structure of the data
  View: what is presented to the user (e.g. ejs files)
  Controller: controls requests of user and genereate appropriate response

- user interacts with view, which genereates appropriate request which is handele by controlller which then renders the appropriate view with Model data as response.

- in this chapter, we will refactor controller layer
- `controllers/newPost.js`

## encrypt the password

- mongoose model hook (hook is just a middleware)
- `npm i bcrypt --save` to encrypt passwords
- [ ] todo: error: bcrypt MODULE_NOT_FOUND
