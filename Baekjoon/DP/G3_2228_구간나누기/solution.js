const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input.shift().split(" ").map(Number);
let arr = Array.from({ length : n }, () => +input.shift());
arr.unshift(0);


let incl = Array.from({ length : n+1 }, () => [0].concat(new Array(m).fill(-1e9)));
let not_incl = Array.from({ length : n+1 }, () => [0].concat(new Array(m).fill(-1e9)));

for (let i=1; i<n+1; i++) {
    for (let j=1; j<Math.min(m, Math.ceil(i/2))+1; j++) {
        not_incl[i][j] = Math.max(incl[i-1][j], not_incl[i-1][j]);
        incl[i][j] = Math.max(incl[i-1][j], not_incl[i-1][j-1]) + arr[i];
    }
}

console.log(Math.max(incl[n][m], not_incl[n][m]));