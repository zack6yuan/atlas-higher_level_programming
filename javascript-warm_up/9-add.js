#!/usr/bin/node
// Node.js script that adds two integers.
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(a, b) {
  return (a + b);
}

let sum = a + b;
console.log(sum);
