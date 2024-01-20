import * as fs from 'fs';
let data = fs.readFileSync('data', 'utf8').split(/\r?\n/);

let bin_gamma: string = "";
let bin_epsilon: string = "";

// transpose array
let d = data.map((_, col) => data.map(row => row[col]));
console.log(d);

