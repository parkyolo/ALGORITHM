const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const [M, N, H] = input[0].split(" ").map(Number);
let tomatos = [];
let idx = 1;
let unriped = 0; // 익지 않은 토마토 개수
let riped = []; // 익은 토마토 위치
for (let i=0; i<H; i++) {
    let box = [];
    for (let j=0; j<N; j++) {
        let line = input[idx++].split(" ").map(Number);
        for (let k=0; k<M; k++) {
            if (line[k] == 0) unriped++;
            else if (line[k] == 1) riped.push([i, j, k]);
        }
        box.push(line);
    }
    tomatos.push(box);
}

let dhrc = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]; // 위치 변화량
let day = 0;
/**
 * queue의 인접한 위치 중 0인 곳을 newQueue에 추가하고 1로 방문 체크하는 함수
 * queue의 길이가 0이되거나 unriped가 0이 되면 함수 종료
 * @param {number[][]} queue 
 */
function BFS(queue) {
    if (queue.length === 0) return; // 새롭게 익은 토마토가 없으면 return
    if (unriped === 0) return; // 남은 안익은 토마토가 없으면 return
    day++;
    newQueue = []; // 새로 익은 토마토
    for (let [h, r, c] of queue) {
        for (let d=0; d<6; d++) { // 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 탐색
            let nh = h+dhrc[d][0];
            let nr = r+dhrc[d][1];
            let nc = c+dhrc[d][2];
            if (nh < 0 || nh >= H || nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (tomatos[nh][nr][nc] === 1 || tomatos[nh][nr][nc] === -1) continue; // 1은 익은 토마토, -1은 토마토가 들어있지 않은 칸
            newQueue.push([nh, nr, nc]);
            tomatos[nh][nr][nc] = 1; // 방문 체크
            unriped --;
        }
    }
    BFS(newQueue);
}

BFS(riped);
BFS()

if (unriped > 0) console.log(-1); // 토마토가 모두 익지는 못하는 상황
else console.log(day); // 토마토가 모두 익을 때까지 걸린 날짜