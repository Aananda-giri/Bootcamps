const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const BlogPostSchema = new Schema({
    title: String,
    body: String,
    // username: String,
    userid: {
        // Relating post collection with user collection
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    datePosted: {/*can declare property type with object like this because we need 'default' */
        type: Date,
        default: new Date()
    },
    image: String
});


const BlogPost = mongoose.model('BlogPost', BlogPostSchema);

// we can export only one variable
module.exports = BlogPost;