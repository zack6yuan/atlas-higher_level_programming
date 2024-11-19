#!/usr/bin/node
// Node.js script that prints number of arguments passed.
let value = 0;
exports.logMe = function (item) {
  console.log(`${value}: ${item}`);
  value++;
};
