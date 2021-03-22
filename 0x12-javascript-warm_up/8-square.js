#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size) === true) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  for (let x = 0; x < size; x++) {
    process.stdout.write('X');
  }
  console.log();
}
