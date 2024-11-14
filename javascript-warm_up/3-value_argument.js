#!/usr/bin/node
// Node.js scripr that prints the first arg passed
if (process.argv.length < 3) {
  console.log('No argument')
} else {
  console.log(process.argv[2])
}
