#!/usr/bin/node
let size;
const arg = [];


process.argv.forEach((val, index) => {
  size = `${index}`;
  arg[index] = `${val}`;
});

if (size <= 2) {
    console.log('0');
}
arg.sort();
console.log(arg[size-1]);