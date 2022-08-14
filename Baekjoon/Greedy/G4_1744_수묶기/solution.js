const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = +input.shift();

let pos_seq = Array.from( {length : N }, () => +input.shift()); // 양수는 내림차순 정렬
let neg_seq = []; // 음수는 오름차순 정렬
pos_seq.sort((a, b) => {return b-a;});
while (pos_seq.length > 0 && pos_seq[pos_seq.length-1] <= 0) {
    neg_seq.push(pos_seq.pop());
}

// console.log(pos_seq, neg_seq); 
let answer = 0;

function cal(seq) {
    let i = 0;
    while (i < seq.length-1) {
        if (seq[i] == 1 || seq[i+1] == 1) { // 1은 곱하지 않고 더하는 게 더 큼
            answer += seq[i];
            i += 1;
        } else { // 앞의 두 수를 곱해서 더함
            answer += seq[i] * seq[i+1];
            i += 2;
        }
    }

    while (i < seq.length) answer += seq[i]; // 남은 수를 더해줌
}

cal(pos_seq);
cal(neg_seq);

console.log(answer);