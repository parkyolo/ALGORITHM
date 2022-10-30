const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const [N, Q] = input[0].split(" ").map(Number);
let nums = input[1].split(" ").map(Number);
nums.unshift(0);
const tree = Array.from({length : (N+1)*4}, () => 0);

function buildTree(start, end, node) {
    if (start == end) return tree[node] = nums[start];
    let mid = Math.floor((start+end) / 2);
    return tree[node] = buildTree(start, mid, node*2) + buildTree(mid+1, end, node*2+1);
}

function getSum(start, end, node, left, right) {
    if (left > end || right < start) return 0;
    if (left <= start && end <= right) return tree[node];
    let mid = Math.floor((start+end)/2);
    return getSum(start, mid, node*2, left, right) + getSum(mid+1, end, node*2+1, left, right);
}

function replaceNum(start, end, node, index, diff) {
    if (index < start || index > end) return;
    tree[node] += diff;
    if (start == end) return;
    let mid = Math.floor((start+end)/2);
    replaceNum(start, mid, node*2, index, diff);
    replaceNum(mid+1, end, node*2+1, index, diff);
}

function game(x, y, a, b) {
    console.log(getSum(0, N, 1, x, y));
    let diff = b-nums[a];
    nums[a] = b;
    replaceNum(0, N, 1, a, diff);
}

buildTree(0, N, 1);

for (let i=2; i<Q+2; i++) {
    let [x, y, a, b] = input[i].split(" ").map(Number);
    if (x > y) [x, y] = [y, x];
    game(x, y, a, b);
}