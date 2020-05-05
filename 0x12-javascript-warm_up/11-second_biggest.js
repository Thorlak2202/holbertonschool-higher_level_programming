#!/usr/bin/node
const size = process.argv.length;
const items = [];
let i = 2;
if (size < 4) {
  console.log(0);
} else {
  for (i; i < size; i++) {
    items.push(parseInt(process.argv[i]));
  }
  const sorted = items.sort(function (a, b) {
    return a - b;
  });
  const rev = sorted.reverse();
  console.log(rev[1]);
}
