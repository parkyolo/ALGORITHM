const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const str = input[0].trim();
const exploe = input[1].trim();
let n = exploe.length;
let stack = new Array(str.length).fill("");
let idx = 0;

for (let i=0; i<str.length; i++) {
    // 1. stack에 새로운 문자열을 넣는다.
    stack[idx++] = str[i];

    // 2. stack의 가장 뒤에 있는 문자열이 폭발 문자열과 일치하면 pop한다.
    //    (index를 이전으로 이동한다.)
    if (stack[idx-1] === exploe[n-1] && idx > n-1) {
        let flag = true;
        for (let j=1; j<n; j++) {
            if (stack[idx-1-j] != exploe[n-1-j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            idx -= n;
        }
    }


}

let result = stack.slice(0, idx).join("");
if (result === "") console.log("FRULA");
else console.log(result);