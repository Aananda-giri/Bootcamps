const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const Schema = mongoose.Schema;

const uniqueValidator = require('mongoose-unique-validator');


const UserSchema = new Schema({
    username:{
        type: String,
        required: [true, "Please provide username."],
        unique: true
    },
    password: {
        type: String,
        required: [true, "Please provide password."]
    },
});


UserSchema.plugin(uniqueValidator); // This will ckeck for duplicate database entries

// change the data before saving any record
UserSchema.pre('save', function(next){
    const user = this
    // hash user.password, 10 indicates password would be hashed 10 times (more rounds of hashing, more slower, more secure)
    bcrypt.hash(user.password, 10, (error, hash) =>{
        user.password = hash;    // replace original password
        next()
    })
})

// export model
const User = mongoose.model('User', UserSchema);

// we can export only one variable
module.exports = User;