#!/usr/bin/node
// Node.js script that defines a square
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
