const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M, K] = input.shift().split(" ").map(Number);
let A = Array.from({length : N}, () => input.shift().split(" ").map(Number));
let copyA = [];
let rotateInfo = Array.from({length : K}, () => input.shift().split(" ").map(Number));

let flag = false;
let minVal = 0; // 배열 A의 값의 최솟값

/**
 * 배열 A의 값(=각 행에 있는 모든 수의 합 중 최솟값)을 구하는 함수
 * @returns valA (배열 A의 값)
 */
function getVal() {
    let valA = copyA[0].reduce((s, v) => s + v, 0);
    for (let i=1; i<N; i++) {
        valA = Math.min(valA, copyA[i].reduce((s, v) => s + v, 0));
    }
    return valA;
}

/**
 * 배열 A를 (rms, cms)부터 (rps, cps)까지 회전시키는 함수
 * 배열을 회전시킬 때에는 시계방향으로 값을 옮기고
 * rms, cms는 1씩 더해주고 rps, cps는 1씩 빼주면서 (rms, cms) === (rps, cps)가 될 때까지 반복한다.
 * @param {number} rms r-s
 * @param {number} cms c-s
 * @param {number} rps r+s
 * @param {number} cps c+s
 * @returns 
 */
function rotateArray(rms, cms, rps, cps) {
    if (rms === rps && cms === cps) return;

    let tmp = copyA[rms][cms];
    // r 증가
    for (let r=rms; r<rps; r++) copyA[r][cms] = copyA[r+1][cms];
    // c 증가
    for (let c=cms; c<cps; c++) copyA[rps][c] = copyA[rps][c+1];
    // r 감소
    for (let r=rps; r>rms; r--) copyA[r][cps] = copyA[r-1][cps];
    // c 감소
    for (let c=cps; c>cms; c--) copyA[rms][c] = copyA[rms][c-1];
    copyA[rms][cms+1] = tmp;

    rotateArray(rms+1, cms+1, rps-1, cps-1);
}

/**
 * 회전 연산의 모든 경우의 수로 배열을 회전시키고 최솟값을 구하는 함수
 * @param {*} rotateOrder 회전 순서
 */
function solution(rotateOrder) {
    copyA = A.map(v => [...v]); // A의 값 deep copy

    for (let idx of rotateOrder) { // rotateOrder대로 배열 회전
        let [r, c, s] = rotateInfo[idx];

        // 배열이 (0, 0)부터 시작하기 때문에 index 조정
        r--; 
        c--;

        rotateArray(r-s, c-s, r+s, c+s); // 배열 회전
    }

    
    let valA = getVal(); // 이번 회전 순서의 배열 A의 값을 구함

    if (!flag) {
        minVal = valA;
        flag = true;
    }
    else minVal = Math.min(minVal, valA); // 최솟값 갱신
}

/**
 * 회전 연산 순서를 구하는 함수
 * @param {Number[]} order 순서를 담는 배열
 * @returns 
 */
function getRotateOrder(order) {
    if (order.length === K) {
        solution(order);     
        return;
    }

    for (let i=0; i<K; i++) {
        if (order.includes(i)) continue;
        order.push(i);
        getRotateOrder(order);
        order.pop();
    }
}

getRotateOrder([]);
console.log(minVal);