const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, p, q] = require("fs").readFileSync(filePath).toString().trim().split(" ").map(Number);

const dict = {}
dict[0] = 1

function dfs(i) {
    if (i in dict) return dict[i];

    return dict[i] = dfs(Math.floor(i/p)) + dfs(Math.floor(i/q));
}

console.log(dfs(n));