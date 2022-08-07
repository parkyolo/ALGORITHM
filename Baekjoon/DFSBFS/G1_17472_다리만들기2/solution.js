// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const [NM, ...mapInput] = input;
const [N, M] = NM.split(" ").map(Number);

let map_ = []
for (let i=0; i<N; i++) {
    let line = mapInput[i].split(" ").map(Number);
    map_.push(line);
}

const dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]];

class Queue {
    constructor() {
        this.storage = {}; // 큐 안의 원소
        this.front = 0; // 첫 원소를 가리키는 포인터
        this.rear = 0; // 마지막 원소를 가리키는 포인터
    }

    size() { // 큐의 크기 구하기
        if (this.storage[this.rear] === undefined) return 0;
        else return this.rear - this.front + 1;
    }

    add(value) {
        if (this.size() === 0) this.storage['0'] = value; // 자바스크립트에서 키 값은 문자열만 가능
        else {
            this.rear += 1;
            this.storage[this.rear] = value;
        }
    }

    popleft() {
        let temp;
        if (this.front === this.rear) { // 데이터가 1개 남은 경우
            temp = this.storage[this.front];
            delete this.storage[this.front];
            this.front = 0;
            this.rear = 0;
        } else {
            temp = this.storage[this.front];
            delete this.storage[this.front];
            this.front += 1;
        }
        return temp;
    }
}

islandNum = 2;
function bfs() {
    for (let r=0; r<N; r++) {
        for (let c=0; c<M; c++) {
            if (map_[r][c] == 1) {
                queue = new Queue();
                queue.add([r, c]);
                map_[r][c] = islandNum;
                while (queue.size()) {
                    let [curX, curY] = queue.popleft();
                    for (let d=0; d<4; d++) {
                        let nextX = curX+dxy[d][0];
                        let nextY = curY+dxy[d][1];
                        if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) continue;
                        if (map_[nextX][nextY] != 1) continue;
                        queue.add([nextX, nextY]);
                        map_[nextX][nextY] = islandNum;
                    }
                }
                islandNum ++;
            }
        }
    }
}

let edges = []; // 섬을 잇는 모든 edge
function getEdges() {
    for (let i=0; i<N; i++) {
        for (let j=0; j<M; j++) {
            if (map_[i][j]) {
                for (let d=0; d<4; d++) {
                    let nextX = i;
                    let nextY = j;
                    let dist = 0;
                    let curNode = map_[i][j];
                    while (true) {
                        nextX += dxy[d][0];
                        nextY += dxy[d][1];
                        dist ++;
                        
                        if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) break;
                        if (map_[nextX][nextY] == curNode) break;
                        if (map_[nextX][nextY]) {
                            let nextNode = map_[nextX][nextY];
                            if (dist > 2) {
                                edges.push([dist-1, Math.min(curNode, nextNode), Math.max(curNode, nextNode)]);
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
}

let parent = []; // 각 노드의 부모 노드
let mst = []; // mst를 만족하는 edge의 가중치

function find_root(x) {
    if (parent[x] == x) return x;
    return parent[x] = find_root(parent[x]);
}

function union_root(x, y) {
    x = find_root(x);
    y = find_root(y);

    if (x != y) parent[y] = x;
}

function kruskal() {
    for (let i=0; i<edges.length; i++) {
        let [dist, firstNode, secondNode] = edges[i];

        if (find_root(firstNode) == find_root(secondNode)) continue; // 사이클 발생

        mst.push([dist, firstNode, secondNode]); // mst에 현재 edge 추가
        union_root(firstNode, secondNode); // parent 갱신

        if (mst.length === islandNum-3) return;
    }
}

bfs(); // 1. 각 섬에 번호 매기기
getEdges(); // 2. 섬을 연결하는 다리들의 길이 구하기
edges.sort(function(a , b) {return a[0]-b[0];}); // 가중치의 오름차순 정렬
parent = Array.from({ length: islandNum }, (v, i) => i) // 부모 노드 초기화
kruskal(); // 3. 크루스칼 알고리즘으로 MST 구하기

let answer = 0; // 구한 가중치의 합
for (let i=0; i< mst.length; i++) {
    answer += mst[i][0];
}

if (mst.length != islandNum-3) console.log(-1); // MST를 만들 수 없을 때(모든 섬을 연결할 수 없을 때)
else console.log(answer);