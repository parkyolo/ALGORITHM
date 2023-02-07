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

let queue = new Deque();
queue.push(n, 0);

let ans = Number.MAX_VALUE;
let visited = Array(10001).fill(false);
visited[n] = true;

while (!queue.isEmpty()) {
    let node = queue.popleft();
    if (node.sec >= ans) continue;
    if (node.x === k) {
        ans = Math.min(ans, node.sec);
        continue;
    }
    if (node.x > k) {
        ans = Math.min(ans, node.sec+node.x-k);
        continue;
    }
    if (node.x*2 <= 100000 && !visited[node.x*2]) {
        visited[node.x*2] = true;
        queue.push(node.x*2, node.sec);
    } if (node.sec+1 < ans) {
        if (node.x-1 >= 0 && !visited[node.x-1]) {
            visited[node.x-1] = true;
            queue.push(node.x-1, node.sec+1);
        } if (node.x+1 <= 100000 && !visited[node.x+1]) {
            visited[node.x+1] = true;
            queue.push(node.x+1, node.sec+1);
        }
    }
}

console.log(ans);