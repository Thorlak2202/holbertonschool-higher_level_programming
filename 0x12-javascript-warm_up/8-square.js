#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number) === true) {
  console.log('Missing size');
}
let x = 0;
for (x; x < number; x++) {
  console.log('x'.repeat(number));
}
