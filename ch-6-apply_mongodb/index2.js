const mongoose = require('mongoose');
const BlogPost = require('./models/BlogPost');

// Connect to MongoDB (add this)
mongoose.connect('mongodb://localhost:27017/my_database', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('Connected to MongoDB');
    // Move the BlogPost.create inside the then() block
    return BlogPost.create({
        "title": "some-title", 
        "body": "some-body"
    });
})
.then((blogPost) => {
    console.log('Blog post created:', blogPost);
})
.catch(error => {
    console.error('Error:', error);
});