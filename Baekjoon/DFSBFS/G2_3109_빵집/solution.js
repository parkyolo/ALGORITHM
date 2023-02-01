const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const dxy = [[-1, 1], [0, 1], [1, 1]];	// 위쪽부터 탐색

const [n, m] = input.shift().split(" ").map(Number);
const board = Array.from({ length : n }, (v, i) => input[i].trim().split(""));

function dfs(r, c) {
    if (c === m-1) return true; // 마지막 열(빵집) 도착

    for (let j=0; j<3; j++) {
        let [nr, nc] = [r+dxy[j][0], c+dxy[j][1]];
        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
        if (board[nr][nc] === 'x' || board[nr][nc] === 'o') continue;
        board[nr][nc] = 'o';    // 방문 체크
        if (dfs(nr, nc)) return true;   // 이 경로로 갈 수 있다면 다음 경로는 확인하지 않고 true 반환
    }
    return false;   // 세 경로 모두 갈 수 없다면 false 반환
}


let cnt = 0;
for (let i=0; i<n; i++) {	// 0번 행부터 탐색
    if (dfs(i, 0)) cnt ++;  // 마지막 열까지 도달했을 때 true가 반환됨
}

console.log(cnt);