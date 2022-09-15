const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const N = +input[0]; // 정점의 개수
let tree = Array.from({length : N+1}, () => new Array); // tree[a] : [[a와 연결된 노드, 간선]]

for (let i=1; i<N; i++) {
    let [node1, node2, weight] = input[i].split(" ").map(Number);
    tree[node1].push([node2, weight]);
    tree[node2].push([node1, weight]);
}

/**
 * startNode에서 exceptNode를 제외한 가장 먼 노드와 거리를 bfs로 탐색하는 함수
 * @param {number} startNode 
 * @param {number} exceptNode 
 * @returns [가장 먼 노드, 거리]
 */
function bfs(startNode, exceptNode) {
    let visited = Array.from({length : N+1}, () => 0);
    visited[startNode] = 1;
    visited[exceptNode] = 1;

    let queue = [[startNode, 0]];
    let farNode = [0, 0];

    while (queue.length) {
        let [curNode, dist] = queue.shift();
        if (farNode[1] < dist) {
            farNode = [curNode, dist];
        }
        for (let [nextNode, nextEdge] of tree[curNode]) {
            if (visited[nextNode]) continue;
            visited[nextNode] = 1;
            queue.push([nextNode, dist+nextEdge]);
        }
    }

    return farNode;
}

// 1. 트리의 지름을 연결하는 두 정점 a와 b를 구하고
let farNodeA = bfs(1, 0); // a
let farNodeB = bfs(farNodeA[0], 0); // b

// 2. a에서 b를 제외한 가장 먼 정점과, b에서 a를 제외한 가장 먼 정점을 구한 후
let farNodeExceptB = bfs(farNodeA[0], farNodeB[0]);
let farNodeExceptA = bfs(farNodeB[0], farNodeA[0]);

// 3. 둘 중 더 큰 거리를 출력
console.log(Math.max(farNodeExceptA[1], farNodeExceptB[1]));