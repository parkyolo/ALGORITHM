// const [S, K] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [S, K] = require('fs').readFileSync('example.txt').toString().trim().split('\n');

let str = ""; // 숫자를 제외한 문자열 저장
for (let i=0; i<S.length; i++) {
    if (isNaN(S[i])) str += S[i];
}

if (str.length < K.length) console.log(0); // 남은 길이가 K보다 짧으면 0 출력
else {
    let flag = 0;
    for (let i=0; i<=str.length-K.length; i++) {
        if (str.substr(i, i+K.length) === K) { // 찾는 문자열이 있으면 flag를 1로 변경
            flag = 1;
            break;
        }
    }
    console.log(flag);
}