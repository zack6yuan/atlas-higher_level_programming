#!/usr/bin/node
// Node.js script that reads and prints file contents.
// Use file system module for operations.
const fs = require('fs');
const file_name = process.argv[2];
fs.readFile(file_name, 'utf-8', (err, data) => {
  if (err) {
    // print error object.
    console.log(err);
  } else {
    // print data.
    console.log(data);
  }
});