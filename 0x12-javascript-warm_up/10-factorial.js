#!/usr/bin/node
const a = parseInt(process.argv[2]);
if (isNaN(a) === true) {
  console.log(1);
} else {
  const fact = function factorial (n) {
    return (n !== 1) ? n * factorial(n - 1) : 1;
  };
  console.log(fact(a));
}
