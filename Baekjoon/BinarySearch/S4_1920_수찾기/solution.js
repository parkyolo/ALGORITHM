const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
const A = input[1].split(' ').map(Number);
const nums = input[3].split(' ').map(Number);
const answer = [];

const BinarySearch = (target, st, en) => {
    
  	// 📌 위에서 말했듯 st와 en은 찾는 수가 있을 수 있는 범위를 나타낸다.
  	// 즉, en이 st보다 작아지면, 그 사이에 수가 존재할 수 없으므로 while문이 종료된다.
    while (en >= st) {
      	// 📌 범위를 절반으로 줄이기 위한 mid를 설정한다.
      	// 근데 여기서 왜 내림을 할까? 아시는 분은 댓글로 알려주세요.
        const mid = Math.floor((st + en) / 2);
    
      	// 📌 target을 찾으면 탐색을 종료한다.
        if (A[mid] === target) {
            return answer.push(1);
        }
        
      	// 📌 A[mid]가 target보다 작으면, A[mid]보다 작거나 같은 범위에는 target이 없다는 것을 의미한다.
      	// 다음 탐색부터는 A[mid]보다 작거나 같은 범위는 탐색에서 제외된다.
      	// 고로, st에 mid보다 큰 값인 mid+1을 할당한다.
        if (A[mid] < target) {
            st = mid + 1;
        } else {
          	// 📌 위 설명과 반대로 이 경우에는 A[mid]보다 큰 범위에 target이 없다는 의미이므로
          	// en에 mid-1을 할당한다.
            en = mid - 1;
        }
    }
    
    return answer.push(0);
}

// 📌 이분 탐색은 반드시 단조증가(감소) 수열에서 이루어져야 한다.
A.sort((a, b) => a - b);
nums.forEach((num) => {
    BinarySearch(num, 0, N-1);
})

console.log(answer.join('\n'));
