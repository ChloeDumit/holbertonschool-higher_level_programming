#!/usr/bin/node
const lastIndex = process.argv.length;
const arg = [];
let newarg = [];

process.argv.forEach((val, index) => {
  arg[index] = val;
});
newarg = [...new Set(arg)];
newarg.sort((a, b) => a - b)
if (lastIndex <= 2) {
    console.log(0);
} else if (lastIndex === 3) {
    console.log(0);
} else {
    console.log(newarg);
    console.log(parseInt(newarg[lastIndex - 2]));
}