let N = require("fs").readFileSync("example.txt").toString().trim().split("\n").map(Number);
// let N = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);

if (N % 5 === 0) {  // 5으로 나누어 떨어질 때
    console.log(N/5);
} else {
    let cnt = 0;
    while (N > 0) {
        N -= 3;
        cnt += 1;
        if (N % 5 === 0) { // 3과 5를 조합해서 담을 수 있을 때
            cnt += N/5;
            console.log(cnt);
            break;
        } else if (N === 1 || N === 2) { // 3과 5로 정확하게 N 킬로그램을 만들 수 없을 때
            console.log(-1);
            break;
        } else if (N === 0) {  // 3으로 나누어 떨어질 때
            console.log(cnt);
            break;
        }
    }
}