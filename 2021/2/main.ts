import * as fs from 'fs';
import {type} from "node:os";
let data = fs.readFileSync('data', 'utf8').split(/\r?\n/);

let pos: number = 0;
let depth:number = 0;

for (let line in data as string[]) {
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
console.log(pos * depth);





