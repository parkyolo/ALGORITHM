const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, L, R] = input[0].split(" ").map(Number);
let board = [];
for (let i=1; i<=N; i++) {
    board.push(input[i].split(" ").map(Number));
}

const dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]];
let cnt = 0;
let visited = [];

function BFS() {
    let flag = false;
    for (let i=0; i<N; i++) {
        for (let j=0; j<N; j++) {
            if (visited[i][j] === 0) {
                let queue = [[i, j]];
                visited[i][j] = 1;
                let unionSize = 1; // 연합을 이루고 있는 칸의 개수
                let unionPopul = board[i][j]; // 연합의 인구수
                let union = [[i, j]]; // 연합을 이루고 있는 칸의 위치
                while (queue.length) { // 인구 차이가 L명 이상, R명 이하인 나라 탐색
                    let [x, y] = queue.shift();
                    for (let k=0; k<4; k++) {
                        let nx = x+dxy[k][0];
                        let ny = y+dxy[k][1];
                        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                        if (visited[nx][ny] === 1) continue;
                        if (Math.abs(board[x][y] - board[nx][ny]) < L || Math.abs(board[x][y] - board[nx][ny]) > R) continue;
                        queue.push([nx, ny]);
                        visited[nx][ny] = 1;
                        unionSize ++;
                        unionPopul += board[nx][ny];
                        union.push([nx, ny]);
                    }
                }
                if (unionSize > 1) { // 인구 이동
                    flag = true;
                    let result = Math.floor(unionPopul/unionSize);
                    for (let [x, y] of union) {
                        board[x][y] = result;
                    }
                }
                
            }
        }
    }
    return flag;
}

while (true) {
    visited = Array.from({length : N}, () => new Array(N).fill(0));
    if (BFS()) cnt ++;
    else break; // 더 이상 인구 이동이 없을 때
}

console.log(cnt);