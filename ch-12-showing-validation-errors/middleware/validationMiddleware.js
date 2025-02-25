// custom form validation middlewawre
module.exports = (req, res, next) =>{
    if(req.files ==null || req.body.title == null || req.body.title ==null){
        return res.redirect('posts/new');   // Redirect back to create post page
    }
    next()
}