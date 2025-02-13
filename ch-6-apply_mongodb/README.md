## apply mongo db

- absulute referencing
  - use `/css/styles.css` instead of `css/styles.css`
- body-parser:
  - middleware that parse incoming resuest bodies in the middleware and make the form data available under the req.body property.
  - `npm install body-parser`

```
const bodyParser = require('body-parser);
app.use(bodyParser.json());
app.user(bodyParser.urlencoded({extended: true}))
```
