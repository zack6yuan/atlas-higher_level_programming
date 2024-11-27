#!/usr/bin/node
/* Node.js script that gets the contents of
a webpage and stores it in a file */
const getRequest = require('request');
// Use file system module for operations.
const fs = require('fs')
const url = process.argv[2];
const path = process.argv[3];
getRequest(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      } else {
        const jsonData = JSON.parse(data);
        console.log(jsonData);
      }
    });
  }
});
