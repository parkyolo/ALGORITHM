const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
// const input = require('fs').readFileSync('example.txt').toString().split('\n');
const [N, L, R, X] = input[0].split(' ').map(Number);
const A = input[1].split(' ').map(Number);
let cnt = 0;
let problems = [];

function checkProblems() {
    let sumOfProblems = problems.reduce((sum, cur) => sum + cur);
    if (sumOfProblems >= L && sumOfProblems <= R && (Math.max(...problems) - Math.min(...problems) >= X)) {
        return true;
    } else {
        return false;
    }
}

function combination(k) {
    if (problems.length >= 2) {
        if (checkProblems())
            cnt ++;
    }

    for (let i=k; i<N; i++) {
        problems.push(A[i]);
        combination(i+1);
        problems.pop();
    }
}

combination(0);

console.log(cnt);