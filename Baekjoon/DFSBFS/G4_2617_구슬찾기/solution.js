const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const graph = Array.from({ length : n+1 }, () => Array.from( { length : 2 }, () => []));

// graph[i][0] : i번 구슬보다 가벼운 구슬
// graph[i][1] : i번 구슬보다 무거운 구슬
for (let i=1; i<m+1; i++) {
    let [a, b] = input[i].split(" ").map(Number);
    graph[a][0].push(b);
    graph[b][1].push(a);
}

let visited = [];

function get_dist(cur, flag) {
    if (graph[cur][flag].length === 0) return 0;    // 1. 리프 노드일 때 count 시작

    let dist = 0;
    for (let next_node of graph[cur][flag]) {       // 2. 모든 자식 노드 탐색
        if (visited[next_node]) continue;           // 3. 이미 방문한 노드이면 continue
        visited[next_node] = true;                  // 4. 방문 체크
        dist += get_dist(next_node, flag) + 1;      // 5. next_node의 자식 노드의 개수 + 자기 자신(1)
    }
    
    return dist;
}

let cnt = 0;
for (let i=1; i<n+1; i++) {
    visited = new Array(n+1).fill(false);	// 방문 배열 초기화

    lighter = get_dist(i, 0);	// 가벼운 구슬의 개수
    heavier = get_dist(i, 1);	// 무거운 구슬의 개수
    if (lighter >= (n+1)/2 || heavier >= (n+1)/2) cnt++;
}

console.log(cnt);