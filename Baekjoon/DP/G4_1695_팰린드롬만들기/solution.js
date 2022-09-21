const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = +input[0];
let seq = input[1].split(" ").map(Number);

// dp[a][b] : a부터 b까지의 부분 수열을 팰린드롬으로 만들기 위해 필요한 원소의 최소 개수
dp = Array.from({length : N}, () => Array.from({length : N}, () => -1));
for (let i=0; i<N; i++) dp[i][i] = 0;

/**
 * a부터 b까지의 부분 수열을 팰린드롬으로 만들기 위해 필요한 원소의 최소 개수를 구하는 함수
 * @param {Number} a 
 * @param {Number} b 
 */
function palindrome(a, b) {
    if (dp[a][b] >= 0) return dp[a][b]; // 이미 dp 값을 구한 범위인 경우
    if (a >= b) return dp[a][b] = 0; // a === b인 경우 dp[a][b]는 항상 0이고, a > b인 경우를 무시해주기 위해 dp[a][b]를 0으로 처리

    if (seq[a] === seq[b]) { // 두 값이 같은 경우
        palindrome(a+1, b-1); // 두 값 사이에 있는 값들의 dp값을 구함
        return dp[a][b] = dp[a+1][b-1];
    } else { // 두 값이 다른 경우
        palindrome(a+1, b); // 왼쪽 값을 제외한 범위의 dp값을 구함
        palindrome(a, b-1); // 오른쪽 값을 제외한 범위의 dp값을 구함
        return dp[a][b] = Math.min(dp[a+1][b], dp[a][b-1])+1; // 둘 중 더 작은 값에 +1
    }
}

console.log(palindrome(0, N-1));