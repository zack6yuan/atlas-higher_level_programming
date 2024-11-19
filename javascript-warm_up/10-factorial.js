#!/usr/bin/node
// Node.js script that computes + prints a factorial.
// Factorial - all the numbers < value but > 0.
const value = parseInt(process.argv[2]);
function getFactorial (value) {
  if (isNaN(value) || value === 0) {
    return 1;
  } else {
    return value * getFactorial(value - 1);
  }
}
console.log(getFactorial(value));
