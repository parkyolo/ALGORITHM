const n = 12 // 14
// const n = +require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')[0];
const mod = 1000000000;

// memo[len][num][state] : 길이가 len이고 1의 자리수가 num이며, 사용한 숫자가 state인 계단 수의 개수
const memo = Array.from(Array(n+1), () => Array.from(Array(10), () => Array(1 << 10).fill(-1)));

function solution(len, num, state) {
    if (len == n) return state == (1 << 10) - 1 ? 1 : 0;            // 0부터 9까지 모두 등장하는 계단 수이면 count
    if (memo[len][num][state] > -1) return memo[len][num][state];   // 이미 방문한 경우
    
    let cnt = 0;    // 1만큼 차이나는 다음 수의 저장된 값
    if (num - 1 >= 0) cnt += solution(len + 1, num - 1, state | (1 << (num - 1)));
    if (num + 1 < 10) cnt += solution(len + 1, num + 1, state | (1 << (num + 1)));

    return memo[len][num][state] = cnt % mod;
}

let result = 0;
for (let i=1; i<10; i++) { // 맨 앞자리에 0이 올 수 없으므로 1~9까지 탐색
    result += solution(1, i, 1 << i);
    result %= mod;
}

console.log(result);