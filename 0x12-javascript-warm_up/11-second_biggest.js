#!/usr/bin/node
const argument = [];
const lastIndex = process.argv.length;
let newArgument = [];

process.argv.forEach((val, index) => {
  argument[index] = val;
});
newArgument = [...new Set(argument)];
newArgument.sort((a, b) => a - b);
if (lastIndex <= 2) { console.log(0); } else if (lastIndex === 3) { console.log(0); } else { console.log(parseInt(newArgument[lastIndex - 2])); }