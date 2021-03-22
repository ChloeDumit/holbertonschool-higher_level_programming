#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(arg1, arg2);
