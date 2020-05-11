#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let y = 0;
    for (y; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
};
