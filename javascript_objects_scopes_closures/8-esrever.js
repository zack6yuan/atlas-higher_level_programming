#!/usr/bin/node
// Node.js script that returns reversed list
exports.esrever = function (list) {
  const reverse = [];
  // iterate over normal list
  for (let x = 0; x < list.length; x++) {
    reverse[x] = list[list.length - 1 - x];
  }
  return reverse;
};
