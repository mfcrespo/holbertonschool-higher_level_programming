#!/usr/bin/node
// Write a script that concats 2 files.
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
if (fileA && fileB && fileC) {
  const fs = require('fs');
  let text = '';
  text = text + fs.readFileSync(fileA);
  text = text + fs.readFileSync(fileB);
  fs.writeFileSync(fileC, text);
}
