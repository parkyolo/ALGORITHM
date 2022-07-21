// const input = require('fs').readFileSync('example.txt').toString().trim();
const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const X = +input;

// X를 이진수로 표현했을 때 1의 개수를 count
let cnt = 0;
for (let i=0; i<=6; i++) {
    if (X & (1<<i)) cnt ++;
}

console.log(cnt);