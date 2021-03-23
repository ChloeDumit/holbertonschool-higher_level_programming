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
  
    print() {
    for(let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
    }
    rotate() {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }

    double () {
        this.width = (this.width * 2);
        this.height = (this.height * 2);
    }
  
  
  
  
  
  }
  module.exports = Rectangle;
    