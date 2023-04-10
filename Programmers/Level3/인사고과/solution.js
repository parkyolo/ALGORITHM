function solution(scores) {
    var answer = 1;    
    let wh = scores[0];

    scores.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        } else {
            return b[0] - a[0];
        }
    });
    
    let threshold = 0;

    for (let [a, b] of scores) {
        if (wh[0] < a && wh[1] < b) return -1;
        if (b >= threshold) {
            if (a + b > wh[0] + wh[1]) answer ++;
            threshold = b;
        }
    }
    
    return answer;
}