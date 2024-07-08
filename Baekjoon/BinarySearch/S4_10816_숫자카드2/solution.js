const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
const A = input[1].split(' ').map(Number);
const nums = input[3].split(' ').map(Number);
const answer = [];

const LowerIndex = (target, st, en) => {
    
    // 📌 현재 찾는 인덱스는 target을 삽입할 수 있는 가장 작은 인덱스이다.
    // st === en이 되어서 삽입 가능한 인덱스가 1개가 되면 반복문을 종료한다.
    while (st < en) {
        const mid = Math.floor((st + en) / 2);
    
        // 📌 A[mid]가 target보다 크거나 같다면,
      	// target이 삽입될 가장 왼쪽 위치일 가능성이 있으므로 (A[mid]의 왼쪽 값이 모두 target보다 작은 경우)
        // en = mid 를 할당한다.
        if (A[mid] >= target) {
            en = mid;
        } 
      	// 📌 A[mid]가 target보다 작으면, target이 삽입될 가장 왼쪽 위치일 가능성이 없음
      	// (여기에 target을 삽입하면 A[mid] 값이 오른쪽으로 밀리면서 정렬이 깨짐)
      	// 그렇기 때문에 다음 반복문에서는 mid보다 큰 범위를 탐색한다.
      	else if (A[mid] < target) {   
            st = mid + 1;
        }
    }
    
    return st;
}

const UpperIndex = (target, st, en) => {
    
    // 📌 위 함수와 반대로 target을 삽입할 수 있는 가장 큰 인덱스(target보다 최초로 큰 수)를 찾는다.
    // st === en이 되어서 삽입 가능한 인덱스가 1개가 되면 반복문을 종료한다.
    while (st < en) {
        const mid = Math.floor((st + en) / 2);
    
      	// 📌 A[mid]가 target보다 작거나 같으면,
      	// 이 위치에 target을 삽입할 경우 정렬이 깨짐
      	// 그러므로 다음 반복문에서는 mid보다 큰 범위만 탐색한다.
        if (A[mid] <= target) {
            st = mid + 1;
        } 
      	// 📌 A[mid]가 target보다 크면,
      	// 이 값이 target보다 최초로 큰 수일 수 있으므로 en = mid를 할당한다.
      	else {
            en = mid;
        }
    }
    
    return st;
}

A.sort((a, b) => a - b);
nums.forEach((num) => {
    answer.push(UpperIndex(num, 0, N) - LowerIndex(num, 0, N));
})

console.log(answer.join(' '));
