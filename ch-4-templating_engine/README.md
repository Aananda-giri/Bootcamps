- Templating engine helps us to dynamically render html pages.
- example templating languages: `handlebars`, `pug`, `EJS`

- `npm install ejs --save`

```
// set ejs as our templating engine that any files ending with .ejs should be rendered with EJS package.
const ejs = require('ejs');
app.set('view engine','ejs');
```

```
// rename `pages` -> views
// rename index.html to index.ejs

app.get('/', (req,res)=>{
    res.sendFile(path.resolve(__dirname, 'pages/index.html'))
})

//instead of above, we can use:
app.get('/', (req,res)=>{
    res.render('index');
})
```

## layouts

- [ejs docs](https://ejs.com/#docs)

* to avoid repetative code (e.g. footer, navBar, ...)

* to run the app: `pnpm start`
