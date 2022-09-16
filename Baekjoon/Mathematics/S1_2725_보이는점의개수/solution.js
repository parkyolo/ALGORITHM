const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const C = +input[0];
const N = [];

for (let i=1; i<=C; i++) {
    N.push(+input[i]);
}

maxN = Math.max(...N);
let coordinateCnt = Array.from({length : maxN+1}, () => 0);
coordinateCnt[1] = 3;

const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);

for (let n=2; n<=maxN; n++) {
    let cnt = 0;
    for (let i=1; i<=n; i++) {
        // x == n이고, 1 <= y <= n일 때
        if (gcd(n, i) == 1) cnt += 1;
        // y == n이고, 1 <= x <= n일 때
        if (gcd(i, n) == 1) cnt += 1;
    }

    coordinateCnt[n] = coordinateCnt[n-1] + cnt;
}

for (let i=0; i<C; i++) {
    console.log(coordinateCnt[N[i]]);
}