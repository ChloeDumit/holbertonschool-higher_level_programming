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
for (let j = 2; j < size; j++) {
    for (let i = 2; i < size; i++) {
        if(arg[i] > arg[i + 1]) {
            let tmp = arg[i];
            arg[i] = arg[i + 1];
            arg[i + 1] = tmp;
        }
    }
}
console.log(arg[size - 1]);