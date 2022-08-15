const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input.shift();
const foods = Array.from({length:N}, () => input.shift().split(" ").map(Number));
let answer = Math.abs(foods[0][0] - foods[0][1]);

function cook(k, arr, sour, bitter) {
    // console.log(k, arr, sour, bitter);
    if (k) answer = Math.min(answer, Math.abs(sour - bitter));

    for (let i=k; i<foods.length; i++) {
        if (!arr[i]) {
            arr[i] = true;
            cook(k+1, arr, sour*foods[i][0], bitter+foods[i][1]);
            arr[i] = false;
        }
    }
}

cook(0, Array.from({length:N}, () => false), 1, 0);
console.log(answer);