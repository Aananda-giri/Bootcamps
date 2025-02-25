const User = require('../models/User.js');
const path = require('path');

module.exports = async (req, res) =>{
    try {
        await User.create(req.body);
        res.redirect('/');
    } catch (error) {
        const validationErrors = Object.keys(error.errors).map(key=> error.errors[key].message);
        req.flash('validationErrors', validationErrors); // This saves `ValidationErrors` key variable to session and flushes at the end of request
        req.flash('data', req.body);    // Save data in case of error (to refill the form instead of reset)
        // req.session.validationErrors = validationErrors;    // Saving to our session makes it accessible to the view
        /*
        This gives something like: ['Path `username` is required', 'Path `password` is required',]
        */
        console.error('Error creating user:', error);
        res.redirect('/auth/register');
    }
}

