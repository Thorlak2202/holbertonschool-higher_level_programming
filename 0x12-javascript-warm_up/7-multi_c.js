#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number) === true) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i; i < number; ++i) {
    console.log('C is fun');
  }
}
