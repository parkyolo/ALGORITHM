const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const state = [""]; // 톱니바퀴의 상태, N극은 0, S극은 1
for (let i=0; i<4; i++) {
    state.push(input[i].trim());
}
const tobniCnt = 8; // 톱니 수
let visited = [];

/**
 * 맞닿은 톱니의 극이 다르면 반대방향으로 회전시키고 num번 톱니바퀴를 회전시키는 함수
 * @param {number} num 회전시킨 톱니바퀴의 번호 
 * @param {number} dir 회전 방향, 1이면 시계 방향, -1이면 반시계 방향
 */
function rotate(num, dir) {
    if (num-1 > 0) { // num-1의 2번 톱니 <-> num의 6번 톱니
        if (!visited[num-1] && state[num-1][2] !== state[num][6]) { // 서로 맞닿은 톱니의 극이 다르면 반대방향으로 회전
            visited[num-1] = 1;
            rotate(num-1, ~dir+1);
        }
    } if (num+1 < 5) { // num의 2번 톱니 <-> num+1의 6번 톱니
        if (!visited[num+1] && state[num][2] !== state[num+1][6]) {
            visited[num+1] = 1;
            rotate(num+1, ~dir+1);
        }
    }
    
    // 톱니 회전
    let curState = state[num];
    state[num] = curState.substring((tobniCnt-dir)%tobniCnt) + curState.substring(0, (tobniCnt-dir)%tobniCnt); // 방향이 1이면 시계 방향, -1이면 반시계 방향으로 회전
}

const K = +input[4];
for (let i=5; i<5+K; i++) {
    let [num, dir] = input[i].split(" ").map(Number); // 회전 방법, [톱니바퀴 번호, 방향]
    visited = [0, 0, 0, 0, 0]; // 방문 체크
    visited[num] = 1;
    rotate(num, dir);
}

// 네 톱니바퀴의 점수의 합을 출력
// (i+1)번 톱니바퀴의 12시 방향이 S극이면 2**i점
let answer = 0;
for (let i=0; i<4; i++) {
    if (state[i+1][0] === "1") answer += 2**i;
}
console.log(answer);