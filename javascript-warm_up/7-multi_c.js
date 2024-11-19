#!/usr/bin/node
// Node.js script that prints x times "C is fun"
const message = 'C is fun';
const iterations = parseInt(process.argv[2]);
if (isNaN(iterations)) {
  console.log('Not a number');
} else {
  for (let x = 0; x < iterations; x++) {
    console.log(message);
  }
}
