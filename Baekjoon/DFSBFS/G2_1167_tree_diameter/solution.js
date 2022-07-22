// const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let V = +input.shift();

// --- N개의 빈 Array로 초기화된 배열 만들기
/*
let tree = [];
for (let i=0; i<V; i++) {
    tree.push([]);
}
*/
let tree = Array.from({ length: V }, () => new Array());

// --- input을 tree 배열에 넣어주기
/*
for (let i=1; i<=V; i++) {
    let node_info = input[i].split(' ').map(Number);
    let curNode = node_info.shift() - 1;
    while (node_info) {
        let nextNode = node_info.shift() - 1;
        if (nextNode === -2) break;
        let distance = node_info.shift();
        tree[curNode].push([nextNode, distance]);
    }
}
*/
input.map((nodeInfo) => {
    let [curNode, ...nextInfo] = nodeInfo.split(' ').map(Number);
    for (let i=0; i<nextInfo.length-1; i+=2) {
        tree[curNode-1].push([nextInfo[i]-1, nextInfo[i+1]]);
    }
})

let answer = {node:0, dist:0};
let visited = Array.from({ length: V }, () => false); // 길이가 V이고 false로 초기화된 배열 생성
visited[answer.node] = true;

function dfs(curNode, distSum) {
    if (distSum > answer.dist) answer = {node:curNode, dist:distSum};

    for (let [nextNode, dist] of tree[curNode]) {
        if (visited[nextNode]) continue;
        visited[nextNode] = true;
        dfs(nextNode, distSum + dist);
        visited[nextNode] = false;
    }
}

dfs(answer.node, 0);
answer.dist = 0;
visited = new Array(V).fill(false); // false로 초기화
visited[answer.node] = true;
dfs(answer.node, 0);

console.log(answer.dist);