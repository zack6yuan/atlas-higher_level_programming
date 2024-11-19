#!/usr/bin/node
// Node.js script that returns number of occurences
exports.nbOccurences = function (list, searchElement) {
  let value = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      value++;
    }
  }
  return (value);
}
