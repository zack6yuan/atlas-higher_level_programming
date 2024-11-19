#!/usr/bin/node
// Node.js script that prints to console.
const check = parseInt(process.argv[2]);
if (isNaN(check)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${check}`);
}
