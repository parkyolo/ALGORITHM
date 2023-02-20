const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const w = input[1].split(" ").map(Number);
const tree = Array.from({ length : n+1 }, () => []);
for (let i=2; i<n+1; i++) {
    let [a, b] = input[i].split(" ").map(Number);
    tree[a].push(b);
    tree[b].push(a);
}

// memo[i][0] : i번 노드가 루트인 서브트리에서 i번 노드를 포함하지 않을 때의 최대 가중치
// memo[i][1] : i번 노드가 루트인 서브트리에서 i번 노드를 포함할 때의 최대 가중치
const memo = Array.from({ length : n+1 }, () => [0, 0]);
const visited = new Array(n+1).fill(false);
const include = new Array(n+1).fill(false);

function dfs(node) {
    // 1. 이번 노드를 포함하면 가중치 추가, 포함하지 않으면 0으로 초기화
    memo[node][0] = 0;
    memo[node][1] = w[node-1];

    for (let next of tree[node]) {
        if (visited[next]) continue;
        visited[node] = true;

        // 2. 다음 노드의 가중치 구하기
        dfs(next);
        // 3. 이번 노드를 포함하지 않으면, 다음 노드의 포함 여부와 관계없이 큰 값을 더함
        memo[node][0] += Math.max(memo[next][0], memo[next][1]);
        // 4. 이번 노드를 포함하면, 다음 노드를 포함하지 않는 경우의 가중치를 더함
        memo[node][1] += memo[next][0];
    }
}

function tracing(node, prev) {
    // 1. 이전 노드를 포함하지 않은 경우 더 큰 값을 path로 저장
    if (memo[node][1] > memo[node][0] && !include[prev]) {
        path.push(node);
        include[node] = true;
    }

    // 2. 다음 노드를 따라감
    for (let next of tree[node]) {
        if (next === prev) continue;
        tracing(next, node);
    }
}

visited[1] = true;
dfs(1);         // 1. 메모이제이션하며 1번 노드가 루트일 때부터 모든 서브트리의 가중치를 구한다.

let path = [];
tracing(1, 0);  // 2. 1번부터 가중치가 큰 노드를 따라가며 경로를 구한다.

let ans = Math.max(memo[1][0], memo[1][1]);
process.stdout.write(ans + "\n");

path.sort(function(a, b) {
	return a - b;
});

for (let node of path) {
    process.stdout.write(node + " ");
}