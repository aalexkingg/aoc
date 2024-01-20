import * as fs from 'fs';
import {type} from "node:os";
let data = fs.readFileSync('data', 'utf8').split(/\r?\n/).map(Number);


let total1 = 0;
let total2 = 0;


// Part 1
data.slice(0).forEach((value, index) => {
    if (value > data[index-1]) {
        total1 += 1
    }
});

// Part 2
data.slice(3).forEach((value, index) => {
    // index starts from 0 of slice
    if (value > data[index]) {
        total2 += 1;
    }
});

console.log("Part 1:", total1);
console.log("Part2:", total2);


