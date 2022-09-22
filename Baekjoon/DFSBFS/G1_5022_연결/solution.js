const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const [a1x, a1y] = input[1].split(" ").map(Number);
const [a2x, a2y] = input[2].split(" ").map(Number);
const [b1x, b1y] = input[3].split(" ").map(Number);
const [b2x, b2y] = input[4].split(" ").map(Number);

let dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]];
let visited = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0)); // 방문 체크
let connected = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0)); // 연결된 전선 저장
let canConnect = false; // (x1, y1)과 (x2, y2)을 이을 수 있다면 true

/**
 * (x1, y1)에서 (x2, y2)로 가는 최단 경로를 구하는 함수
 * @param {Number} x1 
 * @param {Number} y1 
 * @param {Number} x2 
 * @param {Number} y2 
 * @returns 
 */
function bfs(x1, y1, x2, y2) {

    let queue = [[x1, y1, [[x1, y1]]]];
    visited[y1][x1] = 1;
    connected[y1][x1] = 1;

    while (queue.length) {
        let [curX, curY, path] = queue.shift(); // 현재 x좌표, y좌표, 지금까지 지나온 경로

        if (curX === x2 && curY === y2) { // 최단 경로 도착
            canConnect = true; // 두 좌표를 이을 수 있음
            for (let [x, y] of path) { // 전선의 경로 저장
                connected[y][x] = 1;
            }
            return;
        }

        for (let [dx, dy] of dxy) { // 상하좌우 탐색
            let [nextX, nextY] = [curX+dx, curY+dy];
            if (nextX < 0 || nextX > N || nextY < 0 || nextY > M) continue;
            if (visited[nextY][nextX] || connected[nextY][nextX]) continue; // 이미 방문했거나 다른 전선이 지나가는 좌표이면 continue
            visited[nextY][nextX] = 1;
            queue.push([nextX, nextY, path.concat([[nextX, nextY]])]);
        }
    }
}

// A 전선 먼저 연결
visited[b1y][b1x] = 1;
visited[b2y][b2x] = 1;
bfs(a1x, a1y, a2x, a2y);

visited = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0));
connected[b2y][b2x] = 0;
canConnect = false;
bfs(b1x, b1y, b2x, b2y);

let answer = Number.MAX_SAFE_INTEGER;
if (canConnect) answer = connected.reduce((s, v) => s+v.reduce((s, v) => s+v, 0), 0)-2;

// 초기화
visited = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0));
connected = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0));
canConnect = false;

// B 전선 먼저 연결
visited[a1y][a1x] = 1;
visited[a2y][a2x] = 1;
bfs(b1x, b1y, b2x, b2y);

visited = Array.from({length : M+1}, () => Array.from({length : N+1}, () => 0));
connected[a2y][a2x] = 0;
canConnect = false;
bfs(a1x, a1y, a2x, a2y);

if (canConnect) answer = Math.min(answer, connected.reduce((s, v) => s+v.reduce((s, v) => s+v, 0), 0)-2);

if (answer === Number.MAX_SAFE_INTEGER) console.log("IMPOSSIBLE");
else console.log(answer);