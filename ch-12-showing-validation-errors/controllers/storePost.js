const BlogPost = require('../models/BlogPost.js');
const path = require('path');

module.exports = async (req, res) =>{
    let image = req.files.image;
    image.mv(path.resolve(__dirname, '..', 'public/img', image.name))
    console.log(req.body);
    // req.body contains data in format: {"title":"some-title", "body": "some-body"}
    try {
        await BlogPost.create({...req.body, image:'/img/' + image.name});
        res.redirect('/');
    } catch (error) {
        const validationErrors = Object.keys(error.errors).map(key=> error.errors[key].message);
        req.flash('validationErrors', validationErrors);
        req.flash('data', req.body);

        console.error('Error saving post:', error);
        res.redirect('/posts/new');
    }
}

