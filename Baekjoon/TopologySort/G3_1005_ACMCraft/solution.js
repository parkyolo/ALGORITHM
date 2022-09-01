const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

let idx = 0;
const T = +input[idx++]; // 테스트케이스의 개수
let N = 0; // 건물의 개수
let K = 0; // 건설순서 규칙의 개수
let time = []; // 건물당 건설에 걸리는 시간
let order = []; // 건설순서 X, Y
let W = 0; // 백준이가 승리하기 위해 건설해야 할 건물의 번호
let tree = {}; // tree[i] : [[i보다 먼저 지어야 하는 건물], [i보다 늦게 지어야 하는 건물]]
let dp = []; // 건물을 짓는 데 걸리는 최소 시간

/**
 * N, K, time, order, W를 입력받는 함수
 */
function getInput() {
    [N, K] = input[idx++].split(" ").map(Number);
    time = input[idx++].split(" ").map(Number);
    time.unshift(0);
    order = [];
    for (let i=0; i<K; i++) {
        order.push(input[idx++].split(" ").map(Number));
    }
    W = +input[idx++];
}

/**
 * order로 tree를 만드는 함수
 * order : [X, Y] X를 지은 다음에 Y를 짓는 것이 가능하다.
 * tree : [[먼저 지어야 하는 건물], [늦게 지어야 하는 건물]]
 */
function makeTree() {
    tree = {};
    for (let i=1; i<=N; i++) {
        tree[i] = [[],[]];
    }

    for (let [front, back] of order) {
        tree[back][0].push(front);
        tree[front][1].push(back);
    }
}

/**
 * Topology Sort를 실행하는 함수
 */
function topologySort() {
    let queue = []; // 진입 차수가 0인 정점
    for (let i=1; i<=N; i++) {
        if (tree[i][0].length === 0) {
            queue.push(i);
        }
    }

    dp = Array.from({length : N+1}, (v, i) => time[i]); // 건물을 짓는 데 걸리는 최소 시간
    while (queue.length) {
        let curNode = queue.shift();
        for (let nextNode of tree[curNode][1]) {
            dp[nextNode] = Math.max(dp[nextNode], dp[curNode]+time[nextNode]); // dp 갱신
            for (let i=0; i<tree[nextNode][0].length; i++) {
                if (tree[nextNode][0][i] === curNode) { // 현재 node 제거
                    tree[nextNode][0].splice(i, 1);
                    break;
                }
            }
            if (tree[nextNode][0].length === 0) { // 진입 차수가 0이 되면 queue에 추가
                queue.push(nextNode);
            }
        }
    }
}

/**
 * 정답을 출력하는 함수
 */
function getAnswer() {
    console.log(dp[W]);
}

for (let i=0; i<T; i++) {
    getInput();
    makeTree();
    topologySort();
    getAnswer();
}