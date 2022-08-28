const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
let expression = input[1].split('');

// 괄호를 추가하지 않았을 때의 answer 값으로 초기화
let answer = +expression[0];
for (let i=2; i<expression.length; i+=2) {
    if (expression[i-1] === '+') answer += +expression[i];
    else if (expression[i-1] === '-') answer -= +expression[i];
    else answer *= +expression[i];
}

/**
 * 모든 가능한 순서로 수식을 계산해서 최댓값을 갱신하는 함수
 * @param {string[]} arr 현재까지 계산한 수식 배열
 * @param {number} idx arr 계산 시작 index
 * @returns 계산이 끝나면 함수 종료. 아무것도 반환하지 않음
 */
function cal(arr, idx) {
    if (arr.length === 1) {
        answer = Math.max(answer, +arr[0]);
        return;
    } 

    // 현재까지 괄호친 결과를 계산
    let result = +arr[0];
    for (let i=2; i<arr.length; i+=2) {
        if (arr[i-1] === '+') result += +arr[i];
        else if (arr[i-1] === '-') result -= +arr[i];
        else result *= +arr[i];
    }
    answer = Math.max(answer, result);

    // 괄호 추가
    for (let i=idx; i<arr.length-2; i+=2) {
        let subArr = arr.slice(i, i+3);
        let operResult = 0;
        if (subArr[1] === '+') operResult = +subArr[0] + +subArr[2];
        else if (subArr[1] === '-') operResult = +subArr[0] - +subArr[2];
        else operResult = +subArr[0] * +subArr[2];
        cal(arr.slice(0, i).concat([`${operResult}`],arr.slice(i+3)), i+2);
    }
}

cal(expression, 0);
console.log(answer);