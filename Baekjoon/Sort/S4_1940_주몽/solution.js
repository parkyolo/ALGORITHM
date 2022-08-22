const input = require("fs").readFileSync('example.txt').toString().trim().split("\n");
// const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const N = +input[0];
const M = +input[1];
const nums = input[2].split(" ").map(Number);

let cnt = 0;

// 백트래킹 풀이
// function getCombi(material, k) {
//     if (material.length == 2) {
//         if (nums[material[0]] + nums[material[1]] === M) {
//             cnt ++;
            
//         }
//         return;
//     }

//     for (let i=k; i<nums.length; i++) {
//         if (!material.includes(i)) {
//             material.push(i);
//             getCombi(material, i+1);
//             material.pop();
//         }
//     }
// }

// getCombi([], 0);

// 정렬 & 투 포인터 풀이
nums.sort((a, b) => a-b);
console.log(nums);
let left = 0;
let right = nums.length-1;
while (left < right) {
    if (nums[left] + nums[right] === M) {
        cnt ++;
        left ++;
    } else if (nums[left] + nums[right] < M) {
        left ++;
    } else {
        right --;
    }
}

console.log(cnt);