const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input[0];
const T = [0];
const P = [0];
for (let i=1; i<N+1; i++) {
    let [t, p] = input[i].split(" ").map(Number);
    T.push(t);
    P.push(p);
}

const dp = Array.from({length : N+2}, () => 0); // i일에 얻을 수 있는 최대 수익
for (let i=1; i<=N+1; i++) {                    // 1일부터 N+1일까지의 최대 수익을 구함
    dp[i] = Math.max(dp[i], dp[i-1]);                       // 전 날까지 얻은 수익 중 큰 값으로 초기화
    if (i+T[i] <= N+1) {                                    // i일에 상담을 했을 경우 i+T[i]일에 수익이 추가됨
        dp[i+T[i]] = Math.max(dp[i+T[i]], P[i] + dp[i]);    // i+T[i]일의 원래 수익과 상담 후의 수익을 비교
    }
}

console.log(dp[N+1]);   // N+1일의 최대 수익을 출력
    