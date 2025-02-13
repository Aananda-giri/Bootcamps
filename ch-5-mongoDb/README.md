- **installing mongo creates**

* configuration file: /usr/local/etc/mongod.conf
* log directory path: /usr/local/var/log/mongodb
* data directory path: /usr/local/var/mongodb

* running mongod process in the foreground
  `mongod --config /usr/local/etc/mongod.conf`

* mongodb compass: client tool provided by mongoDB team. to see database visually.
  - https://www.mongodb.com/download-center/compass

`npm install mongoose

- connecting to mongoDB from Node

```
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/my_database', {userNewUrlParser: true})

// mongodb will automatically create database for us if it does not already exists.
```

CRUD:

- create, read, update, delete
