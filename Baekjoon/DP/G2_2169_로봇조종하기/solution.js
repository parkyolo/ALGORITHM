const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(filePath).toString().trim().split('\n');

const [n, m] = input.shift().split(" ").map(Number);
const board = Array.from({length:n}, (v, i) => input[i].split(" ").map(Number));
const L_INF = Number.MIN_VALUE;

// worth[i][j] : (i, j)에서의 최대 가치
const worth = Array.from({length:n}, () => Array(m).fill(0));

// 탐색 시작 행 초기화
worth[0][0] = board[0][0];
for (let j=1; j<m; j++) worth[0][j] = worth[0][j-1] + board[0][j];

for (let i=1; i<n; i++) {
    let move2right = Array(m).fill(L_INF);	// 오른쪽으로 이동할 때의 최대 가치
    let move2left = Array(m).fill(L_INF);	// 왼쪽으로 이동할 때의 최대 가치
  
  	// 시작 칸 초기화
    move2right[0] = worth[i-1][0] + board[i][0];
    move2left[m-1] = worth[i-1][m-1] + board[i][m-1];

    for (let j=1; j<m; j++) move2right[j] = Math.max(worth[i-1][j], move2right[j-1]) + board[i][j];		// 위에서 아래로 이동했을 때와 오른쪽으로 이동했을 때의 가치 비교
    for (let j=m-2; j>=0; j--) move2left[j] = Math.max(worth[i-1][j], move2left[j+1]) + board[i][j];	// 위에서 아래로 이동했을 때와 왼쪽으로 이동했을 때의 가치 비교
    for (let j=0; j<m; j++) worth[i][j] = Math.max(move2right[j], move2left[j]);
}

console.log(worth[n-1][m-1]);