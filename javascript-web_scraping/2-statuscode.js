#!/usr/bin/node
/* Node.js script that displays the status
code of a GET request */
const getRequest = require('request');
getRequest(process.argv[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`)
  }
});
