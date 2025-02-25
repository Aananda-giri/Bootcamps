const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const Schema = mongoose.Schema;

const UserSchema = new Schema({
    username:{
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
});

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