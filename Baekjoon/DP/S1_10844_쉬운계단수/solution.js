const N = +require('fs').readFileSync('input.txt').toString().trim();

// memo[i][j] : i번째 수가 j일 때의 계단 수의 개수
const memo = Array.from({length : N+1}, () => Array(10).fill(0));
const mod = 1000000000;

for (let i=1; i<=9; i++) {  // 길이가 1일 때
    memo[1][i] = 1;
}

for (let i=2; i<=N; i++) {
    for (let j=0; j<=9; j++) {
        if (j === 0) memo[i][j] = memo[i-1][1] % mod;
        else if (j === 9) memo[i][j] = memo[i-1][8] % mod;
        else memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1] % mod;
    }
}

let cnt = 0;  // 길이가 N일 때의 계단 수의 개수
for (let j=0; j<=9; j++) {
    cnt = (cnt + memo[N][j]) % mod;
}

console.log(cnt % mod);