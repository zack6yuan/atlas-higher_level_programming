#!/usr/bin/node
// Node.js script that prints the first arg passed
if (process.argv[2] == undefined) {
  console.log('No argument')
} else {
  console.log(process.argv[2])
}
