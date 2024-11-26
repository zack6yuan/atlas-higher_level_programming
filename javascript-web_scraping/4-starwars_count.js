#!/usr/bin/node
/* Node.js script that prints the number of
movies where the charactger "Wedge Antilles"
is present */
const getRequest = require('request');
// Build the URL for the data. + (First argument)
const api = 'https://swapi-api.hbtn.io/api/films' + process.argv[2];
getRequest(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {

  }
});
