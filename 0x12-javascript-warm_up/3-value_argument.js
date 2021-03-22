#!/usr/bin/node
let size;
const arg = [];

process.argv.forEach((val, index) => {
  size = `${index}`;
  arg[index] = `${val}`;
});
if (size < 2) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
