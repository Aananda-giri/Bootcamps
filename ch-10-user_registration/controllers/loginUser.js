const bcrypt = require('bcryptjs');
const User = require('../models/User.js');
const path = require('path');

module.exports = async (req, res) =>{
    const {username, password } = req.body;

    User.findOne({username:username}), (error, user) => {
        if (user){
            bcrypt.compare(password, user.password, (error, user)=>{
                if (same){// if passwords match
                    // store user session
                    res.redirct('/')

                } else {
                    res.redirect('/auth/login')
                }
            })
        } else{
            res.redirect('/auth/login')
        }
    }
    try {
        await User.create(req.body);
        res.redirect('/');
    } catch (error) {
        console.error('Error creating user:', error);
        res.redirect('/auth/register');
    }
}

