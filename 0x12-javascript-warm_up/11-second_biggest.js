#!/usr/bin/node
let size;
const arg = [];
const list = [];
let bigger;

process.argv.forEach((val, index) => {
  size = `${index}`;
  arg[index] = `${val}`;
});

if (size <= 2) {
    console.log('0');
}
bigger = arg[2];
for(let i = 2; i <= size; i++) {
  if (arg[i] > bigger) {
    for (let j = 0; j <= size; j++) {
      list[j] = arg[i];
      bigger = arg[i];
      
    }
    
  }
}
console.log(list);