const mongoose = require('mongoose');
const BlogPost = require('./models/BlogPost');

// Connect and create (in your main script)
mongoose.connect('mongodb://localhost/my_database')
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .then(blogpost => {
    console.log('Blog post created:', blogpost);
  })
  .catch(error => {
    console.error('Error:', error);
  });


// Create new blog post document
const mongoose = require('mongoose');

// Define the schema (in a separate file, e.g., models/BlogPost.js)
const blogPostSchema = new mongoose.Schema({
    title: String,
    body: String
});

const BlogPost = mongoose.model('BlogPost', blogPostSchema); // 'BlogPost' is the collection name

// Connect and create (in your main script)
mongoose.connect('mongodb://localhost/my_database', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('Connected to MongoDB');
    return BlogPost.create({  // Return the Promise for chaining
        title: "The mythbuster's Guide to saving money on energy bills",
        body: "If you have been here a long time, you might remember when i wnee on ITV ..."
    });
  })
  .then(blogpost => {
    console.log('Blog post created:', blogpost);
  })
  .catch(error => {
    console.error('Error:', error);
  });



// find all documents
BlogPost.find({});


// or to find document iin BlogPost Collection with 'The' in title
// '/' acts as %, which gets single database document
BlogPost.find({title:/The/})

// find by id
var id = "<long-id>"
BlogPost.findById(id);

//updating records
var id = "<long-id>"
BlogPost.findByIdAndUpdateid(id, {
    title: 'Updated title'
})

// Delete single record
var id = "<long-id>"
BlogPost.findByIdAndDelete(id)

