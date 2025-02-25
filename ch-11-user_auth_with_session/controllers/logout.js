module.exports = (req,res) =>{
    // Destroy session data including session user id, We then redirect to home page
    req.session.destroy(()=>{
        res.redirect('/')
    })
}