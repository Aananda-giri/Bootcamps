- [source](https://www.youtube.com/watch?v=TlB_eWDSMt4)

backend

paypal, uber, netflix

- node is c++ program that contains chrome v8 js engine
- built spring based app in node and
  node app built 2\* faster, fewer people,
  - js everywhere
  - source code would be cleaner because: js on front end and back end
  - large eco system of open source libraries

runtime env to execute js app

## how node works

- non blocking, async nature of node
- waiter can serve two customers
- node should not be used for cpu intensive applications
- node applications are single threaded, serving one client, other clients have to wait. so no cpu intensive applications.

node --version

- install from nodejs.org (install latest stable version)

## First node application

- `first_app/`

## Modules

```
console.log();  // global
setTimeout()
clearTimeout()

setInterval()
clearInterval()

window.console.log()
console.log()

var message = '';
global.setTimeout
console.log(global)

```

## Modules

- by default this defines globally

* evey file in node is considered module
* variables/functions inside that file/module are private to that file/module. to use that outside that module, we have to export it.
* Every node application have at least one file/module which we call main module
* it is possible to define two same function name in two files
* avoid defining variables in global scope

```
  var sayHello = function () {

}

window.sayHello();
```

## Creating a module

file: `logger.js`

- better to define imported variable to constant so that we dont over-write it. e.g. `const logger = require('./logger');`

## Event: signal that indicate something has happened in our application.

e.g. http class raises an event when new user send request

- class: first char fo every word is capital

// normal function

```
function (arg) {

}
```

arrow function

```
(arg) => {

}
```

// Raise: logging (data: message)

-

## Extending event emitter

- `third_app/`
- class that have all the capabilities of event emitter and that you would use in your class.
