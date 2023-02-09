// 가중치, (x, y) 좌표를 저장할 node
class Node {
    constructor(v, x, y) {
        this.v = v;
        this.x = x;
        this.y = y;
    }
}


// 우선순위 큐
class PriorityQueue {
    constructor() {
        this.heap = [ null ];
    }
    
    size() {
        return this.heap.length - 1;
    }
    
    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    
    heappush(v, x, y) {
        let data = new Node(v, x, y);
        this.heap.push(data);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while (curIdx > 1 && this.heap[parIdx].v > this.heap[curIdx].v) {
            this.swap(parIdx, curIdx)
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    
    heappop() {
        const min = this.heap[1];
        if (this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();   
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1; 
        
        if (!this.heap[leftIdx]) return min;
        if (!this.heap[rightIdx]) {
            if (this.heap[leftIdx].v < this.heap[curIdx].v) {
                this.swap(leftIdx, curIdx);
            }
            return min;
        }

        while (this.heap[leftIdx].v < this.heap[curIdx].v || this.heap[rightIdx].v < this.heap[curIdx].v) {
            const minIdx = this.heap[leftIdx].v > this.heap[rightIdx].v ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
            if (leftIdx >= this.heap.length || rightIdx >= this.heap.length) break;
        }

        return min;
    }
}


// 풀이
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]];
let idx = 0;  // input의 index
let pnum = 1; // 문제 번호

let n;
while (n = +input[idx++]) {
    solution(n);
}

function solution(n) {
    let cave = Array.from({ length : n }, () => input[idx++].split(" ").map(Number));
    let dist = Array.from({ length : n }, () => new Array(n).fill(-1));
    dist[0][0] = cave[0][0];

    let queue = new PriorityQueue();  // 우선순위 큐 생성
    queue.heappush(cave[0][0], 0, 0);
    
    while (queue.size()) {
        let node = queue.heappop();         // 1. queue에서 가장 가중치가 작은 node를 꺼냄
        let [v, x, y] = [node.v, node.x, node.y];
        if (x === n-1 && y === n-1) break;  // 2. (n-1, n-1)에 도달하면 종료

        for (let d=0; d<4; d++) {           // 3. 네 방향을 탐색
            let [nx, ny] = [x+dxy[d][0], y+dxy[d][1]];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

            let nv = v+cave[nx][ny];        // 4. 다음 가중치를 구함

            if (nv < dist[nx][ny] || dist[nx][ny] === -1) {
                dist[nx][ny] = nv;          // 5. 첫 방문하거나 가중치가 작을 경우만 갱신
                queue.heappush(nv, nx, ny); // 6. 새로운 node를 queue에 넣어줌
            }
        }
    }

    console.log("Problem %d: %d", pnum++, dist[n-1][n-1]);
}