#!/usr/bin/node
let arg1= process.argv[2];

function factorial(n) {
  

  if (isNaN(n) === true) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(arg1));