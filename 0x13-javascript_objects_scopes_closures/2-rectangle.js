#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0 || this.width === undefined || this.height === undefined) {
      const NewRec = require('./0-rectangle');
      const R1 = new NewRec();
      return R1;
    }
  }
}
module.exports = Rectangle;
