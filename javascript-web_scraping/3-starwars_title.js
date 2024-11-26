#!/usr/bin/node
/* Node.js script that prints the title of a
Star Wars movie where the episode number
matches a given integer */
const getRequest = require('request');
// Build the URL for the data. + (First argument)
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
getRequest(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const json_data = JSON.parse(body);
    console.log(json_data.title);
  }
});
