const EventEmitter = require('events');

var url = 'http://mylogger.io/log';

class Logger extends EventEmitter{
    log(message){
        // send an HTTP request
        console.log(message);

        // Rise an event
        this.emit("MessageLogged", {id:1, url: 'https://'});
    }
}
module.exports = Logger;