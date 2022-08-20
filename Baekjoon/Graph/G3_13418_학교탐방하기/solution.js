const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

let enter = 0; // 출발 간선이 오르막이면 1, 내리막이면 0
const [N, M] = input.shift().split(" ").map(Number);
const uphill = []; // 오르막길을 연결한는 노드 쌍
const downhill = []; // 내리막길을 연결하는 노드 쌍

for (let i=0; i<M+1; i++) {
    let [A, B, C] = input[i].split(" ").map(Number);
    if ((A === 0 || B === 0)) {
        if (C === 0) enter ++; // 출발 간선이 오르막일 때
     }
    else if (C === 0) uphill.push([A, B]);
    else downhill.push([A, B]);
}

function find_root(x) {
    if (parent[x] == x) return x;
    return parent[x] = find_root(parent[x]);
}

function union_root(x, y) {
    x = find_root(x);
    y = find_root(y);

    if (x != y) parent[y] = x;
}

let parent = [];
let mst = Array.from({length : 2}, () => new Array); // 1: 오르막, 0: 내리막

function kruskal(firstEdges, secondEdges, minmax) { // minmax 0: 최소 개수, 1 : 최대 개수
    for (let i=0; i<firstEdges.length; i++) {
        let [firstNode, secondNode] = firstEdges[i];
        if (find_root(firstNode) == find_root(secondNode)) continue;
        mst[minmax].push(minmax);
        union_root(firstNode, secondNode);

        if (mst[minmax].length === N-1) return;
    }

    for (let i=0; i<secondEdges.length; i++) {
        let [firstNode, secondNode] = secondEdges[i];
        if (find_root(firstNode) == find_root(secondNode)) continue;
        mst[minmax].push(~minmax+2);
        union_root(firstNode, secondNode);

        if (mst[minmax].length === N-1) return;
    }
}

parent = Array.from({length : N+1}, (v, i) => i);
kruskal(downhill, uphill, 0);

parent = Array.from({length : N+1}, (v, i) => i);
kruskal(uphill, downhill, 1);

let minUphill = mst[0].reduce((sum, val) => sum + val, 0) + enter;
let maxUphill = mst[1].reduce((sum, val) => sum + val, 0) + enter;
console.log(maxUphill**2 - minUphill**2);