const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [t, ...testcases] = input;

function solution(t, testcases) {
    for (let i=0; i<t; i++) {
        let idx = Number(testcases[i*2].split(' ')[1]);
        let queue = testcases[i*2+1].split(' ').map(i=>Number(i));

        let cnt = 1;
        while (true) {
            let front = queue.shift();
            if (Math.max(...queue) <= front && idx == 0) {
                console.log(cnt);
                break;
            } else if (Math.max(...queue) > front && idx == 0) {
                queue.push(front);
                idx = queue.length - 1; // 문서의 index가 맨 뒤로 감
            } else if (Math.max(...queue) > front && idx > 0) {
                queue.push(front);
                idx--; // 문서가 한 칸 앞으로 감
            } else if (Math.max(...queue) <= front) {
                cnt ++;
                idx--;
            }
        }
        
    }
}

solution(t, testcases);