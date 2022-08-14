class PriorityQueue {
    constructor() {
      this.queue = [null];
    }
  
    size() {
        return this.queue.length;
    }
  
    enqueue(priority) {
      this.queue.push(priority);
  
      let curIdx = this.size()-1;
      let parentIdx = Math.floor(curIdx/2);
      while (this.queue[parentIdx] && curIdx > 1 && this.queue[parentIdx] < this.queue[curIdx]) { // 부모의 우선 순위가 더 작다면 swap
          [this.queue[curIdx], this.queue[parentIdx]] = [this.queue[parentIdx], this.queue[curIdx]];
          curIdx = parentIdx;
          parentIdx = Math.floor(curIdx/2);
      }
    }
  
    dequeue() {
      if (this.size() === 1) return 0;
  
      let result = this.queue[1];
  
      if (this.size() === 2) this.queue = [null];
      else this.queue[1] = this.queue.pop();
  
      let curIdx = 1;
      let leftIdx = curIdx*2;
      let rightIdx = curIdx*2 + 1;
  
      if (this.queue[leftIdx] === null) return result; // 자식이 없는 경우
  
      if (this.queue[rightIdx] === null) { // 자식이 하나인 경우
          if (this.queue[curIdx] < this.queue[leftIdx]) {
              [this.queue[curIdx], this.queue[leftIdx]] = [this.queue[leftIdx], this.queue[curIdx]];
          }
          return result;
      }
  
      while ((this.queue[leftIdx] && this.queue[curIdx] < this.queue[leftIdx]) || (this.queue[rightIdx] && this.queue[curIdx] < this.queue[rightIdx])) {
          let largestIdx = 0;
  
          if (this.queue[rightIdx]) {
              largestIdx = this.queue[leftIdx] < this.queue[rightIdx] ? rightIdx : leftIdx;
          } else {
              largestIdx = leftIdx;
          }
  
          [this.queue[curIdx], this.queue[largestIdx]] = [this.queue[largestIdx], this.queue[curIdx]];
          curIdx = largestIdx;
          leftIdx = curIdx*2;
          rightIdx = curIdx*2 + 1;
      }
  
      return result;
    }
  }

const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, K] = input.shift().split(" ").map(Number);
const jewelry = [];
const bags = [];
for (let i=0; i<N; i++) jewelry.push(input[i].split(" ").map(Number));
for (let i=N; i<N+K; i++) bags.push(Number(input[i]));

jewelry.sort((a, b) => a[0] - b[0]);
bags.sort((a, b) => a - b);

let answer = 0;
let idx = 0; // 몇 번째 보석까지 담았는지 체크하는 index
const priorityQueue = new PriorityQueue();

for (bag of bags) {
    for (let i = idx; i < jewelry.length; i++) {
      if (jewelry[i][0] <= bag) { // 보석의 무게가 가방의 최대 무게보다 작으면
        idx++;
        priorityQueue.enqueue(jewelry[i][1]); // 우선순위 큐에 보석의 가격 삽입
      }
      else {
        break;
      }
    }
    answer += priorityQueue.dequeue(); // 가장 높은 가격이 반환됨
}

console.log(answer);