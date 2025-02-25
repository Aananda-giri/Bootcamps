const BlogPost = require('../models/BlogPost.js');
const path = require('path');

module.exports = async (req, res) =>{
    let image = req.files.image;
    image.mv(path.resolve(__dirname, '..', 'public/img', image.name))
    console.log(req.body);
    // req.body contains data in format: {"title":"some-title", "body": "some-body"}
    try {
        await BlogPost.create({
            ...req.body,
            image:'/img/' + image.name,
            userid: req.session.userId
        });
        res.redirect('/');
    } catch (error) {
        console.error('Error saving post:', error);
        res.redirect('/posts/new');
    }
}

