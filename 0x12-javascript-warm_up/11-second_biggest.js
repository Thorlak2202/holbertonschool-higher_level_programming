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
  const rev = items.reverse();
  console.log(rev[1]);
}
