let [p, q, a, n] = require("fs").readFileSync('example.txt').toString().trim().split(" ").map(Number);
// let [p, q, a, n] = require("fs").readFileSync('/dev/stdin').toString().trim().split(" ").map(Number);

let answer = 0;

/**
 * 최소공배수를 구하는 함수
 * @param {number} num1 첫 번째 정수
 * @param {number} num2 두 번째 정수
 * @returns num1과 num2의 최소공배수
 */
function getLCM(num1, num2) {
    const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
    const lcm = (a, b) => a * b / gcd(a, b);
    return lcm(num1, num2);
}

/**
 * 단위 분수를 구하는 함수
 * 1/1부터 1/(a/mul)까지의 단위분수를 분할에 추가하면서(남은 수에서 빼주면서)
 * 분자가 0이 되어 모두 단위분수로 분할되었다고 판단될 때 answer를 증가한다.
 * @param {number} numer 분자
 * @param {number} denom 분모
 * @param {number} unit 단위분수의 분모
 * @param {number} mul 단위분수의 분모의 곱
 * @param {number} cnt 단위분수의 개수
 */
function getUnitFraction(numer, denom, unit, mul, cnt) {
    let lcm = getLCM(denom, unit);                  // 1. 남은 수의 분모와 단위분수의 분모의 최소공배수를 구한다.
    numer = numer*(lcm/denom) - 1*(lcm/unit);       // 2. 남은 수에서 단위분수를 뺀 분자를 구한다.
    denom = lcm;                                    // 3. 분모는 최소공배수가 된다.

    mul *= unit;                                    // 4. 1/unit의 단위분수를 분할했기 때문에 mul에 곱해준다.
    cnt += 1;                                       // 5. 분할한 개수를 증가시킨다.

    if (numer < 0 || mul > a || cnt > n) return;    // 6. 분자가 0보다 작아지거나 분모의 곱이 a보다 커지거나 분할한 개수가 n보다 커지면 종료

    if (numer == 0) {                               // 7. 분자가 0이 되면 모든 수가 단위분수로 분할 되었다는 의미이다.
        answer ++;
        return;
    }

    if (denom % numer == 0) {                       // 8. 남은 분모가 분자로 나누어 떨어지면 기약분수로 나눠준다.
        denom /= numer;
        numer = 1;
    }
    
    for (let i=unit; i<=Math.floor(a/mul)+1; i++) { // 9. 다음 단위분수로 분할한다.
        getUnitFraction(numer, denom, i, mul, cnt);
    }
}

for (let i=1; i<=a; i++) {
    getUnitFraction(p, q, i, 1, 0);
}

console.log(answer);
