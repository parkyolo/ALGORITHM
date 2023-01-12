const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +input[0];
const cost_matrix = [];
for (let i=1; i<=n; i++) cost_matrix.push(input[i].split(" ").map((el) => +el));
const memo = Array.from({length:n}, () => Array(1<<n).fill(-1)); // memo[i][j] : i에서 출발해서 j만큼 방문했을 때의 최소 비용

function get_dist(node, path) {
    if (path == (1<<n)-1) return cost_matrix[node][0] ? cost_matrix[node][0] : Number.MAX_VALUE; // node에서 출발점으로 돌아갈 수 없는 경우 max 값 반환

    if (memo[node][path] > -1) return memo[node][path]; // 이미 방문한 node인 경우

    memo[node][path] = Number.MAX_VALUE; // 첫 방문 노드 초기화
    for (let i=0; i<n; i++) {
        if (cost_matrix[node][i] == 0 || path & 1<<i) continue; // node에서 i로 갈 수 없거나 i를 이미 방문한 노드인 경우
        
        let next_path = path | 1<<i; // i번 방문까지 포함한 다음 경로
        memo[node][path] = Math.min(memo[node][path], get_dist(i, next_path) + cost_matrix[node][i]);
    }

    return memo[node][path];
}

console.log(get_dist(0, 1));