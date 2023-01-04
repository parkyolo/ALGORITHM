const input = require('fs').readFileSync('example.txt').toString().trim().split('\n')[0];

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')[0];

function solution(input) {
    if (input[0] == '0') return 0;  // 0으로 시작하는 암호일 경우

    const dp = new Array(input.length).fill(1);

    for (let i=1; i<input.length; i++) {
        if (input[i] == '0') {
            if (input[i-1] == '0') return  0;   // 00인 경우

            if (+input.slice(i-1,i+1) < 27) {   // 10, 20
                if (i == 1) dp[i] = dp[i-1];
                else dp[i] = dp[i-2];
            } else {                            // 30, 40, 50 등의 숫자
                return 0;
            }
        } else {
            if (input[i-1] == '0') dp[i] = dp[i-1]; // 이전 숫자가 0인 경우 가짓수 동일
            else if (+input.slice(i-1,i+1) < 27) {  // 이전 숫자와 결합하여 해석될 수 있는 경우
                if (i == 1) dp[i] = (dp[i-1] + 1) % 1000000;
                else dp[i] = (dp[i-2] + dp[i-1]) % 1000000;
            } else {                                // 이전 숫자와 결합할 수 없는 경우 가짓수 동일
                dp[i] = dp[i-1];
            }
        }
       
    }

    return dp[input.length-1];
}

const answer = solution(input);
console.log(answer);