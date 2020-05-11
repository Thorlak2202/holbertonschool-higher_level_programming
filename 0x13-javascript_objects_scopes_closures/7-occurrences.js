#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let k = 0;
  for (i in list) {
    if (list[i] === searchElement) {
      k += 1;
    }
  }
  return (k);
};
