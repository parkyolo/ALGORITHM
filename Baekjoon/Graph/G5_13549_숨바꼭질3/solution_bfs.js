class Node {
    constructor(x, sec) {
        this.x = x;
        this.sec = sec;
    }
}

class Deque {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    isEmpty() {
        if (this.length === 0) return true;
        else return false;
    }

    push(x, sec) {
        let node = new Node(x, sec);
        if (this.length === 0) this.head = node;
        else this.tail.next = node;
        this.tail = node;
        this.length++;
    }

    popleft() {
        let item = this.head;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
        }
        this.length--;
        return item;
    }
}

const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, k] = require("fs").readFileSync(filePath).toString().trim().split(" ").map(Number);

let ans = Number.MAX_VALUE;

let queue = new Deque();
queue.push(n, 0);

let visited = Array(10001).fill(false);
visited[n] = true;

while (!queue.isEmpty()) {	// BFS 탐색
    let node = queue.popleft();
  	let [x, s] = [node.x, node.sec];
  
    if (s >= ans) continue;	// 경과 시간이 ans보다 커지면 넘어감
    if (x >= k) {
        // x가 k보다 크거나 같아지면 ans 갱신
      	// x가 k보다 커지면 x-1로 이동하는 경우만 남기 때문에 더이상 덱에 넣지 않는다.
        ans = Math.min(ans, s+x-k);
        continue;
    }
  
  	for (let [nx, ns] of [[x*2, s], [x-1, s+1], [x+1, s+1]]) {	// 세 방향 탐색
      if (0 <= nx <= 100000 && !visited[nx]) {	// 범위 안에 있고 아직 방문하지 않은 위치여야 함
        visited[nx] = true;
        queue.push(nx, ns);
      }
    }
}

console.log(ans);