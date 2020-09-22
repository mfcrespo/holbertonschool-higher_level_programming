#!/usr/bin/node
// Write a class Rectangle that defines a rectangle

module.exports = class Rectangle {
	constructor (w, h) {
	  if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	  }
	}
      
	print () {
	  for (let i = 0; i < this.height; i++) {
	    for (let j = 0; j < this.width; j++) {
	      process.stdout.write('X');
	    }
	    process.stdout.write('\n');
	  }
	}
      
	rotate () {
	  let temp = this.height;
	  this.height = this.width;
	  this.width = temp;
	}
      
	double () {
	  this.width *= 2;
	  this.height *= 2;
	}
      };
