module.exports = (req, res) =>{
    console.log('calling newPost');
    if (req.session.userId){
        res.render('create', {
            createPost: true
        });
    } else {
        res.redirect('/auth/login');
    }
}
