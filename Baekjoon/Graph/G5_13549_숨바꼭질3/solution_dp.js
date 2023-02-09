class Node {
    constructor(x, sec) {
        this.x = x;
        this.sec = sec;
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
    
    heappush(x, sec) {
        let data = new Node(x, sec);
        this.heap.push(data);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while (curIdx > 1 && this.heap[parIdx].sec > this.heap[curIdx].sec) {
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
            if (this.heap[leftIdx].sec < this.heap[curIdx].sec) {
                this.swap(leftIdx, curIdx);
            }
            return min;
        }

        while (this.heap[leftIdx].sec < this.heap[curIdx].sec || this.heap[rightIdx].sec < this.heap[curIdx].sec) {
            const minIdx = this.heap[leftIdx].sec > this.heap[rightIdx].sec ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
            if (leftIdx >= this.heap.length || rightIdx >= this.heap.length) break;
        }

        return min;
    }
}

const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, k] = require("fs").readFileSync(filePath).toString().trim().split(" ").map(Number);

let queue = new PriorityQueue();
queue.heappush(n, 0);

let visited = Array(100001).fill(-1);
visited[n] = 0;

while (queue.size()) {	// Dijkstra 탐색
    let node = queue.heappop();
  	let [x, s] = [node.x, node.sec];
  
    if (x === k) {  // x가 k에 도달하면 종료
        console.log(s);
        break;
    }
  
  	for (let [nx, ns] of [[x*2, s], [x-1, s+1], [x+1, s+1]]) {	// 세 방향 탐색
      if (0 <= nx <= 100000 && (visited[nx] === -1 || visited[nx] > ns)) {	// 범위 안에 있고 현재보다 가중치가 작아야 함
        visited[nx] = ns;
        queue.heappush(nx, ns);
      }
    }
}