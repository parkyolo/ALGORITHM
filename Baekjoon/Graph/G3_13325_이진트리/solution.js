const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const k = +input[0];
const edgeWeights = input[1].split(" ").map(Number);

const weightSum = Array.from({length : 2**(k+1)-2}, (a, i) => edgeWeights[i]); // 현재 엣지에서 리프까지 거리의 최댓값
function getWeightSum(h) { // 높이가 h인 트리의 리프 노드를 기준으로 부모 노드에 최대 가중치를 더해 줌
    if (h == 1) return;
    for (let idx=2**h-2; idx<2**(h+1)-2; idx+=2) {
        weightSum[Math.floor(idx/2)-1] += Math.max(weightSum[idx], weightSum[idx+1]);
    }
    getWeightSum(h-1);
}

function getWeight(idx) {
    let curIdx = idx ? weightSum[idx] < weightSum[idx+1] : idx+1; // 증가시켜야 할 idx
    edgeWeights[curIdx] += Math.abs(weightSum[idx] - weightSum[idx+1]); // 거리를 같게 만들기 위해 필요한 차이만큼 더해줌
    if (idx > 2**k-3) return;
    getWeight((idx+1)*2);
    getWeight((idx+1+1)*2);
}

getWeightSum(k); // 모든 노드를 기준(루트)으로 리프까지의 거리의 최댓값을 구함
getWeight(0); // 형제 노드와 비교해서 거리가 더 작은 노드의 가중치를 증가시켜서 모든 거리를 같도록 함
console.log(edgeWeights.reduce((sum, val) => sum+val, 0));