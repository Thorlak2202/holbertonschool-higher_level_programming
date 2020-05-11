#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let y = 0;
    for (y; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }
};
