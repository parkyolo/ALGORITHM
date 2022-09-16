const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
let inputExpression = input[1].trim();

let flag = false; // answer이 초기화되었는지 확인
let answer = 0;

/**
 * 수식에서 모든 연산자를 이용한 연산을 하나씩 수행하고(괄호를 추가하고) 그 결과로 다시 함수를 호출해서 숫자만 남을 때까지 반복하는 함수
 * expression이 숫자일 경우 answer을 최댓값으로 갱신하고 종료
 * @param {String} expression 연산할 수식
 * @returns None
 */
function calculate(expression) {
    if (!isNaN(expression)) { // 숫자만 남은 경우(= 연산이 끝난 경우)
        if (!flag) { // 아직 answer을 초기화하지 않았다면
            answer = +expression; // 연산 결과로 초기화
            flag = true;
        }
        else answer = Math.max(answer, +expression); // answer을 최댓값으로 갱신
        return;
    }

    let i = 0;
    
    let firstOperand = ""; // 첫 번째 피연산자
    let startIdx = i; // 첫 번째 피연산자의 시작 index
    
    if (expression[i] === "-") firstOperand += expression[i++]; // 음수인 경우
    while (!isNaN(expression[i])) firstOperand += expression[i++]; // expression[i]가 숫자이면 firstOperand에 더해줌

    while (i < expression.length) {
        let secondOperand = ""; // 두 번째 피연산자
        let secondIdx = 0; // 두 번째 피연산자의 시작 index

        let exResult = ""; // 연산 결과
        let operator = ""; // 연산자
   
        operator = expression[i++];
        secondIdx = i;
        if (expression[i] === "-") secondOperand += expression[i++]; // 음수인 경우
        while (!isNaN(expression[i])) secondOperand += expression[i++]; // 숫자이면 더해줌
        let endIdx = i; // 연산이 끝난 index

        if (operator === "+") exResult = String(+firstOperand + +secondOperand);
        else if (operator === "-") exResult = String(+firstOperand - +secondOperand);
        else exResult = String(+firstOperand * +secondOperand);

        let nextEx = expression.substring(0, startIdx) + exResult + expression.substring(endIdx); // 다음 수식
        calculate(nextEx);

        firstOperand = secondOperand; // 다음 연산의 첫 번째 연산자
        startIdx = secondIdx;
    }
}

calculate(inputExpression);
console.log(answer);