class Node {
    constructor(x, y, w, c, day) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.c = c;
        this.day = day;
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

    push(x, y, w, c, day) {
        let node = new Node(x, y, w, c, day);
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
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]];

const [n, m, k] = input.shift().split(" ").map(Number);
const board = Array.from({length:n}, (v, i) => input[i].trim().split("").map(Number));
const visited = Array.from({length:n}, () => Array(m).fill(k+1));

let queue = new Deque();
queue.push(0, 0, 0, 1, true); // (x, y, w, c, day) : x좌표, y좌표, 부순 벽의 개수, 이동 거리, day는 낮이면 true
visited[0][0] = 0;

while (!queue.isEmpty()) {
    let node = queue.popleft();

    if (node.x == n-1 && node.y == m-1) {   // (n, m) 도착
        console.log(node.c);
        break;
    }

    for (let i=0; i<4; i++) {
        let nx = node.x + dxy[i][0];    // 다음 위치 (nx, ny)
        let ny = node.y + dxy[i][1];
        
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;   // 범위를 벗어나면 continue
        
        let nw = node.w + board[nx][ny];           // (nx, ny)가 벽인 경우 +1
        if (nw >= visited[nx][ny]) continue;       // 벽을 더 적게 부수고 지나간 적이 있다면 continue
        
        if (board[nx][ny] === 1 && !node.day) {    // (nx, ny)가 벽인데 밤일 경우
            queue.push(node.x, node.y, node.w, node.c+1, !node.day);
            continue;
        }

        visited[nx][ny] = nw;
        queue.push(nx, ny, nw, node.c+1, !node.day);
    }
}

if (visited[n-1][m-1] === k+1) console.log(-1); // (n, m)에 도달할 수 없는 경우