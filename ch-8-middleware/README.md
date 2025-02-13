# Chapter 8: Express Middlewares

- functions express executes in the middle after request which produce output that can be final output or be used by next middleware.

- express-fileupload

- `npm install --save express-fileupload`

```
e.g.
app.use(express.static('public'))
app.use(bodyParser.json())
```

## Custom middleware

```
// index.js
const customMiddleWare = (req, res, next) => {
    console.log("Custom middleware called");
    next()
}
app.use(customMiddleWare)

// "Custom middleware called" will be displayed every time you refresh the app.

// apply this middleware for specific url pattern (specific request).
app.use('posts/store', validateMiddleWare);
```

- Good use case: form validation
