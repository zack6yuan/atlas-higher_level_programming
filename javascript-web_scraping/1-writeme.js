#!/usr/bin/node
// Node.js script that writes a string to a file.
// Use file system module for operations.
const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];
fs.writeFIle(filePath, stringWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data)
  }
});
