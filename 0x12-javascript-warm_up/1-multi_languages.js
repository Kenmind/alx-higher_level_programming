#!/usr/bin/node
let myVar = 'C is fun';
let i;
for (i = 1; i < 4; i++) {
  if (i === 2) { myVar = 'Python is cool'; }
  if (i === 3) { myVar = 'JavaScript is amazing'; }
  console.log(myVar);
}

