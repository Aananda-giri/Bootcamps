module.exports = (req, res) =>{
    console.log('calling newPost');
    if (req.session.userId){
        res.render('create');
    } else {
        res.redirect('/auth/login');
    }
}
