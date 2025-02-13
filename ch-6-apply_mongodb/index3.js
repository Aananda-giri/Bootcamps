const express = require('express');
const mongoose = require('mongoose');
const app = express();

// Middleware for parsing form data
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Connect to MongoDB first
mongoose.connect('mongodb://localhost:27017/my_database', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('Connected to MongoDB');
})
.catch(error => {
    console.error('MongoDB connection error:', error);
});

// Import your model after connection setup
const BlogPost = require('./models/BlogPost');

// Your route handler
app.post('/post/store', async (req, res) => {
    try {
        await BlogPost.create(req.body);
        res.redirect('/');
    } catch (error) {
        console.error('Error saving post:', error);
        res.redirect('/posts/new');
    }
});

// Start server AFTER MongoDB connection
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});