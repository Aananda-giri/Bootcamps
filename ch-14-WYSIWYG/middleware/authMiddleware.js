const User = require('../models/User');

module.exports = (req,res, next) => {
    try {
        const user = User.findById(req.session.userId);

        if (user){
                console.log(`authMiddleware success user: ${user}`);
                next();
            
        } else {
            console.log(`authMiddleware user not found user: ${user}`);
            return res.redirect('/');
        }
    } catch(error){
        console.log(`error in authMiddleware: ${error}`);
            return res.redirect('/');
    }
}