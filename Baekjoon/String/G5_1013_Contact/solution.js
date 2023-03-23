const regex = /^(100+1+|01)+$/;

const input = require('fs').readFileSync('input.txt').toString().trim().split('\n');
const T = +input[0];

for (let i=1; i<T+1; i++) {
    let str = input[i].trim();
    if (regex.test(str)) console.log("YES");
    else console.log("NO");
}