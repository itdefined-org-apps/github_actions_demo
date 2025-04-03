let express = require("express")
let app = express()
app.get('/', (req, res)=>{
    res.send('<h1> Welcome to Express!!!</h1>')
})
app.listen(3000)