#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x) === true) {
  console.log('Missing number of occurrances');
}
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
