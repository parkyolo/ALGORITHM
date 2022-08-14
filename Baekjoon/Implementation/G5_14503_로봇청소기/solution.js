// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const [N, M] = input.shift().split(" ").map(Number);
let [r, c, d] = input.shift().split(" ").map(Number); // 로봇 청소기의 좌표 (r, c), 바라보는 방향 d
let board = Array.from({ length: N }, () => input.shift().trim().split(" ").map(Number));

let areaCnt = 0; // 청소한 영역의 개수

// 0: 북, 1: 동, 2: 남, 3:서
const drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

label:
while (true) { // 0: 빈 칸, 1: 벽, 2: 이미 청소한 공간
    
    // 현재 위치 청소
    if (board[r][c] == 0) {
        board[r][c] = 2; 
        areaCnt ++;
    }
    
    // console.log(r, c, d);

    // 현재 위치에서 현재 방향을 기준으로 왼쪽방향 탐색
    for (let i=0; i<4; i++) {
        // 다음 방향 0 -> 3, 1 -> 0, 2-> 1, 3 -> 2
        let nd = (d+3)%4;
        let nr = r+drc[nd][0];
        let nc = c+drc[nd][1];
        if (board[nr][nc] === 0) { // 왼쪽 방향에 청소하지 않은 공간이 있는 경우
            // 한 칸 전진, 방향 회전
            r = nr;
            c = nc;
            d = nd;
            continue label;
        } else {
            d = nd;
        }
    }
    
    // 왼쪽 방향에 청소할 공간이 없는 경우
    bd = d > 1 ? d-2 : d+2; // 0 -> 2, 1 -> 3, 2 -> 0, 3 -> 1
    let br = r+drc[bd][0];
    let bc = c+drc[bd][1];
    if (board[br][bc] != 1) { // 한 칸 후진
        r = br;
        c = bc;
    } else { // 뒤쪽 방향이 벽이라 후진할 수 없는 경우
        break;
    }
}

console.log(areaCnt);