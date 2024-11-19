#!/usr/bin/node
// Node.js script that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    print() {
      for (let x = 0; x < this.width; x++) {
        console.log('X');
      }
      for (let y = 0; y < this.height; y++) {
        console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
