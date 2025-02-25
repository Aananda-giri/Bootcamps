const bcrypt = require('bcryptjs')
const User = require('../models/User')

module.exports = async (req, res) => {
    const { username, password } = req.body;
    
    try {
        // Use await instead of callback
        const user = await User.findOne({ username: username });
        
        if (user) {
            // Use Promise-based bcrypt.compare rather than callback
            const same = await bcrypt.compare(password, user.password);
            
            if (same) { // if passwords match
                // store user session
                console.log(`user found. password-matched username and password. \n session: ${req.session}`);
                req.session.userId = user._id;
                res.redirect('/');
            } else {
                console.log('user found. password did-not-matched username and password');
                res.redirect('/auth/login');
            }
        } else {
            console.log("could not find user. redirecting to /auth/login::\n user:", user);
            res.redirect('/auth/login');
        }
    } catch (error) {
        console.error("Error during login:", error);
        res.status(500).redirect('/auth/login');
    }
}