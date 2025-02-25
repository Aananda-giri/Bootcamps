module.exports = (req, res) =>{
   
    // To refill data when reloading due to error
    var username=""
    var password=""
    const data=req.flash('data')[0];

    if (typeof data != "undefined"){
        username = data.username
        password = data.password
    }
    res.render('register', {
        errors: req.flash('validationErrors'),
        username: username,
        password: password
        // errors: req.session.validationErrors   // Retrive error from session with req.session.validationErrors and pass it to register.ejs
    }) // render register.ejs
}