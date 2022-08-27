const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const board = [];
for (let i=1; i<=N; i++) {
    board.push(input[i].split(" ").map(Number));
}

const visited = Array.from({length : N}, () => new Array(M).fill(0));
const dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]];

let answer = 0;
function dfs(x, y, cnt, sum) {
    if (cnt === 4) {
        answer = Math.max(answer, sum);
        return;
    }

    for (let k=0; k<4; k++) {
        let nx = x+dxy[k][0];
        let ny = y+dxy[k][1];
        if (nx < 0 || nx >= N || ny < 0 || ny >=  M) continue;
        if (visited[nx][ny]) continue;
        visited[nx][ny] = 1;
        dfs(nx, ny, cnt+1, sum+board[nx][ny]);
        visited[nx][ny] = 0;
    }
}

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        visited[i][j] = 1;
        dfs(i, j, 1, board[i][j]);
        // ㅜ 모양 처리
        if (i+2 < N && j-1 >= 0) {
            let sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j-1];
            answer = Math.max(answer, sum);
        }
        if (i+2 < N && j+1 < M) {
            let sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1];
            answer = Math.max(answer, sum);
        }
        if (i+1 < N && j-1 >= 0 && j+1 < M) {
            let sum = board[i][j] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1];
            answer = Math.max(answer, sum);
        }
        if (i+1 < N && j+2 < M) {
            let sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1];
            answer = Math.max(answer, sum);
        }
        visited[i][j] = 0;
    }
}

console.log(answer);