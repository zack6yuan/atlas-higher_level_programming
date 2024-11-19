#!/usr/bin/node
// Node.js script that converts a number
// From base 10 to another base (argument)
exports.converter = function (base) {
  return function myConverter (x) {
    return x.toString(base);
  };
};
