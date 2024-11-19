#!/usr/bin/node
// Node.js script that prints x times "C is fun"
const message = 'C is fun';
let iterations = parseInt(process.argv[2]);
for (let x = 0; x < iterations; x++) {
  console.log(message);
}
