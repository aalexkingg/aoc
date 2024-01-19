import * as fs from 'fs';
import {type} from "node:os";
let data = fs.readFileSync('data', 'utf8').split(/\r?\n/);

let pos: number = 0;
let depth:number = 0;

// Part 1
for (let line of data as string[]) {
    let [dir, dist] = line.split(" ");

    if (dir == "forward") {
        pos += Number(dist);
    }
    else if (dir == "up") {
        depth -= Number(dist);
    }
    else {
        depth += Number(dist);
    }
}
console.log("Part 1:", pos * depth);

// Part 2
let aim: number = 0;
pos = 0;
depth = 0;

for (let line of data as string[]) {
    let [dir, dist] = line.split(" ")

    if (dir == "down") {
        aim += Number(dist);
    }
    else if (dir == "up") {
        aim -= Number(dist);
    }
    else {
        pos += Number(dist);
        depth += Number(dist) * aim;
    }
}
console.log("Part 2:", pos * depth);