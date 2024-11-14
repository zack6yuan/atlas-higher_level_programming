#!/usr/bin/node
// Node.js script that prints the first arg passed
if (process.argv.length < 3) {
  console.log('No argument')
} else {
  console.log(process.argv[2])
}
// can't use 'length'