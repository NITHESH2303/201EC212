const express = require('express');
const mongoose = require('mongoose');
const app = express();

mongoose.connect('mongodb://localhost:27017/myapp', {useNewUrlParser: true});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
