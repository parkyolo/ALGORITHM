// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const [R, C] = input.shift().split(" ").map(Number);
let map_ = Array.from({ length: R }, () => input.shift().trim().split(""));
const dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]];


let changeLand = []; // 바다로 바뀔 땅
for (let x=0; x<R; x++) {
    for (let y=0; y<C; y++) {
        if (map_[x][y] === 'X') {
            let cnt = 0; // 바다와 인접한 칸의 개수
            for (let i=0; i<4; i++) {
                let nx = x+dxy[i][0];
                let ny = y+dxy[i][1];
                if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                    cnt ++;
                    continue;
                } 
                if (map_[nx][ny] === '.') cnt ++;
            }
            if (cnt == 3 || cnt == 4) changeLand.push([x, y]);
        }
        
    }
}

for (let [x, y] of changeLand) { // 잠긴 땅 갱신
    map_[x][y] = '.';
}

let [startR, startC, endR, endC] = [R-1, C-1, 0, 0]; // 남은 땅의 범위
for (let x=0; x<R; x++) {
    for (let y=0; y<C; y++) {
        if (map_[x][y] === 'X') {
            startR = Math.min(startR, x);
            startC = Math.min(startC, y);
            endR = Math.max(endR, x);
            endC = Math.max(endC, y);
        }
    }
}

let resultMap = Array.from({ length : endR - startR + 1}, () => new Array()); // 새로운 지도
for (let x=startR; x<=endR; x++) {
    for (let y=startC; y<=endC; y++) {
        resultMap[x-startR].push(map_[x][y]);
    }
}

for (let i=0; i<resultMap.length; i++) {
    console.log(resultMap[i].join(''));
}