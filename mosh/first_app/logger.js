console.log(__filename); // <file_path>/logger.js
console.log(__dirname); // <file_path>

var url='http://mylogger.io/log'

function log(message){
    // private to this module
    // send an HTTP request
    console.log(message);
}


// make it visible from outside
module.exports = log;

/*
module.exports.log = log;

const logger = require('./logger');
logger.log('message')
*/

// module.exports.endPoint = url;   // export url as endPoint