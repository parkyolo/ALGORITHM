const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const [a, b, c] = input[0].split(" ").map(Number);
const N = +input[1];

let parts = Array.from({length : a+b+c+1}, () => 2);
let failParts = [];
for (let i_=2; i_ < input.length; i_++) {
    let [i, j, k, r] = input[i_].split(" ").map(Number);
    if (r === 1) { // 3개의 부품 모두 정상
        parts[i] = 1;
        parts[j] = 1;
        parts[k] = 1;
    } else {
        failParts.push([i,j,k]);
    }
}

let flag = true; // 새로 고장으로 분류된 부품이 있을 경우 true
while (flag) {
    let temp = [];
    flag = false;
    for (let i_=0; i_<failParts.length; i_++) {
        const [i, j, k] = failParts[i_];
        // 3개의 부품 중 2개가 정상이라면, 나머지 1개는 고장
        if (parts[i] == 1 && parts[j] == 1) {
            flag = true;
            parts[k] = 0;
        } else if (parts[j] == 1 && parts[k] == 1) {
            flag = true;
            parts[i] = 0;
        } else if (parts[k] == 1 && parts[i] == 1) {
            flag = true;
            parts[j] = 0;
        } else {
            temp.push(failParts[i_]);
        }
    }
    failParts = temp;
}

for (let i=1; i<parts.length; i++) {
    console.log(parts[i]);
}