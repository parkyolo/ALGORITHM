const N = Number(require("fs").readFileSync('example.txt').toString().trim());
// const N = Number(require("fs").readFileSync('/dev/stdin').toString().trim());

// 움직이는 횟수는 공비가 2인 등비수열의 합
let K = 1*(2**N-1);
// let k = 0;
let answer = [];

function hanoi(num, from, other, to) {
    if (num === 0) {
        return
    }
    hanoi(num-1, from, to, other); // N번째 막대를 to로 보내려면 N-1개의 나머지 막대를 other로 보내야 함
    answer.push([from, to]); // 나머지 막대를 모두 other로 보낸 후에 N번째 막대를 to로 보냄
    // k++;
    hanoi(num-1, other, from, to); // other로 보냈던 막대들을 다시 to로 보냄
}


hanoi(N, "1", "2", "3");
console.log(K);
console.log(answer.map((v) => v.join(" ")).join("\n"));