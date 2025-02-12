const path = require('path');

var pathObj = path.parse(__filename);

console.log(pathObj);
/*
{
  root: '/',
  dir: '<other-dir-path>/mosh/second_app',
  base: 'app.js',
  ext: '.js',
  name: 'app'
}
*/


console.log(`Total Memory: ${totalMemory}`);

// ----------
// os module
// ----------
const os = require('os');

var totalMemory = os.totalmem();
var freeeMemory = os.freemem();

// console.log('Total MEmory: ' + totalMemory);

// Template string
// ES^ / ES2015 : ECMAScript 6

console.log(`Total Memory: ${totalMemory}`);
console.log(`Free Memory: ${totalMemory}`);


// ------------
// File system
// ------------
const fs = require('fs');
const files = fs.accessSync('./'); // sync are blocking (always use async)

console.log(files);


fs.readdir('./', function(err, files){
    if (err) console.log('Error', err);
    else console.log('Result', files);
});



// --------
// Events
// --------

// class: first char fo every word is capital
const EvevntEmitter = require('events');
const { EventEmitter } = require('stream');

const emitter = new EventEmitter(); // object
// class is like human and object is like actal person

// we have to register a listner that listens for this emit
emitter.on('messageLogged', function(arg){  // sometimes also refered as: e, eventArg
    console.log('Listner called', arg);
})

// emit means making a noise/produce something
emitter.emit('messageLogged', {id: 1, url: 'http://'});  // above callback function is called

