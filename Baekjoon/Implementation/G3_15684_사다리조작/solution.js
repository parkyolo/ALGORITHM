const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");
const [n, m, h] = input[0].split(" ").map(Number);
const board = Array.from({ length : h+1 }, () => new Array(n+1).fill(0));
for (let i=1; i<m+1; i++) {
    let [a, b] = input[i].split(" ").map(Number);
    board[a][b] = 1;
}

let maxCnt = 0;
let minCnt = 4;

function playGame() {
    // player는 (1, i)에서 (h+1, i)로 이동 (1 <= i <= n)
    for (let i=1; i<n+1; i++) {
        let [y, x] = [1, i];
        while (y < h+1) {

            // 오른쪽(y, x)에 가로선이 있다면 오른쪽 아래로 이동
            // 왼쪽(y, x-1)에 가로선이 있다면 왼쪽 아래로 이동
            if (board[y][x]) x++;
            else if (board[y][x-1]) x--;
            y++;
        }
        if (x != i) return false;
    }

    return true;
}

// (y, x) : 가로선 위치 (1 <= y <= h, 1 <= x < n)
function dfs(cnt) {
    if (maxCnt >= minCnt) return;
    if (maxCnt === cnt) {
        if (playGame()) minCnt = Math.min(minCnt, cnt);
        return;
    }
    
    for (let x=1; x<n; x++) {
        for (let y=1; y<=h; y++) {
            // 가로선을 추가할 수 없는 경우
            if (board[y][x] || board[y][x-1] || board[y][x+1]) continue;

            // 가로선 추가
            board[y][x] = 1;
            dfs(cnt+1);
            board[y][x] = 0;

            // 이미 방문한 칸은 지나가기
            while (y <= h && !board[y][x-1] && !board[y][x+1]) y++;
        }
    }
}

// 추가 가로선은 0개에서 3개까지 가능
for (let i=0; i<4; i++) {
    dfs(0);
    maxCnt ++;
}

if (minCnt === 4) minCnt = -1; 
console.log(minCnt);