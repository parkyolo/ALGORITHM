const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");

const N = +input.shift();
let state = []; // 현재 번호 안내판의 상태
for (let i=0; i<4*N; i+=4) {
    let num = '';
    for (let j=0; j<5; j++) {
        num += input[j].substring(i, i+3).trim();
    }
    state.push(num);
}

// 0~9 숫자 상태
nums = ['####.##.##.####', '..#..#..#..#..#', '###..#####..###', '###..####..####', '#.##.####..#..#', '####..###..####', '####..####.####', '###..#..#..#..#', '####.#####.####', '####.####..####'];

let can_express = []; // can_express[i] : i번째 안내판이 나타내고 있다고 볼 수 있는 번호
let cnt = 1; // 전체 경우의 수

for (let i=0; i<N; i++) {
    cur_num = state[i];
    cur_case = [];
    for (let j=0; j<10; j++) {
        compare_num = nums[j];
        flag = true;
        for (let k=0; k<15; k++) {
            if (cur_num[k] == '#' && compare_num[k] == '.') {
                flag = false;
                break;
            }
        }
        if (flag) {
            cur_case.push(j);
        }
    }
    can_express.push(cur_case);
    cnt *= cur_case.length; // 가능한 번호가 없는 경우, 경우의 수는 0이 됨
}

if (cnt == 0) console.log(-1); // 가능한 층 번호가 없는 경우
else {
    let sum = 0;

    for (let i=0; i<N; i++) {
        cur_length = can_express[i].length;
        for (let num of can_express[i]) {
            // 숫자는 10^(n-i-1)자리 수를 가리킴
            // 숫자가 반복되는 횟수(cnt/cur_length)만큼 더해줌
            sum += num*10**(N-i-1)*(cnt/cur_length);
        }
    }
    
    console.log(sum/cnt);
}
