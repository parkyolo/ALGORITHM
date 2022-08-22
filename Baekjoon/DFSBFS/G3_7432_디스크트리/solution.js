const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
const fullPath = [];
for (let i=1; i<=N; i++) {
    fullPath.push(input[i].trim().split("\\"));
}

function getPath(path, blank) {
    let root = [];
    let nextPath = {};

    for (let i=0; i<path.length; i++) {
        if (path[i].length === 0) continue;
        let preDir = path[i].shift();
        if (preDir in nextPath) {
            nextPath[preDir].push(path[i]);
        } else {
            root.push(preDir);
            nextPath[preDir] = [path[i]];
        }
    }

    root.sort();
    for (firstDir of root) {
        console.log(blank+firstDir);
        getPath(nextPath[firstDir], blank+" ");
    }
}

getPath(fullPath, "");