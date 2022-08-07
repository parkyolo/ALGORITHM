const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');

let board = [];
for (let i=0; i<10; i++) {
    let line = input[i].split(" ").map(Number);
    board.push(line);
}

let paper = [0, 5, 5, 5, 5, 5]; // 남은 색종이의 개수
let answer = 101;

function updateBoard(x, y, size, state) { // state : 0 -> 색종이 붙이기, 1 -> 색종이 떼기
    for (let i=x; i<x+size; i++) {
        for (let j=y; j<y+size; j++) {
            board[i][j] = state;
        }
    }
} 

function canAttachPaper(x, y, size) { // x+size, y+size가 범위 안에 들어오고, 모두 1일 때
    if (x+size > 10 || y+size > 10) return false;
    for (let i=x; i<x+size; i++) {
        for (let j=y; j<y+size; j++) {
            if (board[i][j] == 0) return false;
        }
    }
    return true;
}

function dfs(x, y, cnt) {
    if (x >= 9 && y > 9) { // (x, y)가 board의 끝일 때
        answer = Math.min(answer, cnt); // answer 갱신
        return;
    }
    if (answer <= cnt) return; // 현재 cnt가 최솟값이 될 수 없을 때

    if (y > 9) { // 현재 행의 끝에 도달했을 때, 다음 행으로 넘어감
        dfs(x+1, 0, cnt);
        return;
    }
    
    if (board[x][y] == 1) {
        for (let size=5; size>0; size--) { // 큰 색종이부터 붙일 수 있는지 탐색
            if (paper[size] > 0 && canAttachPaper(x, y, size)) { // 길이가 size인 종이가 남아있고, x+size, y+size가 범위 안에 들어오고, 모두 1일 때
                updateBoard(x, y, size, 0); // size만큼을 0으로 (색종이 붙이기)
                paper[size] --;
                dfs(x, y+1, cnt+1);
                updateBoard(x, y, size, 1); // size만큼을 다시 1로 (색종이 떼기)
                paper[size] ++;
            }
        }
    } else {
        dfs(x, y+1, cnt);
    }
}

dfs(0, 0, 0);
if (answer == 101) console.log(-1);
else console.log(answer);