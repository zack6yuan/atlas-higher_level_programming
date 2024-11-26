#!/usr/bin/node
/* Node.js script that computes the number
of tasks completed by user id */
const getRequest = require('request');
const fs = require('fs');
const apiURL = 'https://jsonplaceholder.typicode.com/todos' + process.argv[2];
getRequest(apiURL, (error, response, body) => {
  if (err) {
    console.log(err);)