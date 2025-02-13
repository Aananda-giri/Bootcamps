- [template](https://startbootstrap.com/theme/clean-blog)

* nodemon that auto detect code changes and auto restart the server

npm install nodemon --save-dev
// save lists dependencies reflected on package.json
// dev indicates for development purpose only and not on deployment

```
// package.json
"scripts": {
    "start": "nodemon index.js"
}
```

// instead of running with `node index.js` we can do `node start`
