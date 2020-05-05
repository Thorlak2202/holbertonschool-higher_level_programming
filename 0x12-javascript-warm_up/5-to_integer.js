#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
