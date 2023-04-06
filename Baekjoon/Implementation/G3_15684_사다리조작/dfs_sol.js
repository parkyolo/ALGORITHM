const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n");
const [n, m, h] = input[0].split(" ").map(Number);
const board = Array.from({ length : h }, () => new Array(n-1).fill(0));
for (let i=1; i<m+1; i++) {
    let [a, b] = input[i].split(" ").map(Number);
    board[a-1][b-1] = 1;
}

let minCnt = 4;

function playGame() {
    // player는 (1, i)에서 (h+1, i)로 이동 (1 <= i <= n)
    for (let i=1; i<n+1; i++) {
        let [y, x] = [1, i];
        while (y < h+1) {

            // 오른쪽(y-1, x-1)에 사다리가 있다면 오른쪽 아래로 이동
            // 왼쪽(y-1, x-2)에 사다리가 있다면 왼쪽 아래로 이동
            if (board[y-1][x-1] === 1) x++;
            else if (x-2 >= 0 && board[y-1][x-2] === 1) x--;
            y++;
        }
        if (x != i) return false;   // 
    }

    return true;
}

// (y, x) : 사다리를 놓을 위치 (0 <= y < h, 0 <= x < n-1)
function dfs(y, x, cnt) {   
    if (cnt > 3) return;
    if (y === h) {
        if (playGame()) minCnt = Math.min(minCnt, cnt);
        return;
    }
    
    // 사다리를 새로 놓지 않는 경우
    if (x+1 < n-1) dfs(y, x+1, cnt);
    else if (x+1 === n-1) dfs(y+1, 0, cnt);

    // 사다리를 새로 놓을 수 없는 경우 return
    if (board[y][x] === 1) return;
    if (x-1 > 0 && board[y][x-1] === 1) return;
    if (x+1 < n-1 && board[y][x+1] === 1) return;

    // 사다리를 새로 놓는 경우
    board[y][x] = 1;
    if (x+1 < n-1) dfs(y, x+1, cnt+1);
    else if (x+1 === n-1) dfs(y+1, 0, cnt+1);
    board[y][x] = 0;
}

dfs(0, 0, 0);
if (minCnt === 4) console.log(-1);
else console.log(minCnt);