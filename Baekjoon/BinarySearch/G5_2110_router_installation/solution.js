// const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let [NC, ...XX] = input;
let [N, C] = NC.split(' ').map(Number);
let X = XX.map(Number).sort((a,b) => a - b);

let max_dist = 0;
let start = 0;
let end = X[N-1];
let mid = 0;
let pre = X[0];

while (start <= end) {
    mid = Math.floor((start+end)/2);
    pre = X[0];
    let cnt = 1;
    for (let i=1; i<N; i++) {
        if (X[i] - pre >= mid) {
            pre = X[i];
            cnt ++;
        }
    }

    if (cnt >= C) {
        max_dist = mid;
        start = mid+1;
    } 
    else end = mid-1;
}

console.log(max_dist);