const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, m, k] = require("fs").readFileSync(filePath).toString().trim().split(" ").map(Number);

function combination(n, r) { // nCr
    let result = 1;
    for (let i=n; i>n-r; i--) result *= i;
    for (let i=1; i<=r; i++) result /= i;
    return result;
}

function divide(a, z, k) {  // a의 개수, z의 개수, k번째 문자열
    if (a === 0 || z === 0) {   // a만 남거나 z만 남으면 만들 수 있는 문자열은 1가지
        let answer = "";
        for (let i=0; i<a; i++) answer += "a";
        for (let i=0; i<z; i++) answer += "z";
        return answer;
    }

    let cnt = combination(a+z-1, Math.min(a-1, z)); // a가 앞에 올 때 만들 수 있는 조합의 개수
    if (k <= cnt) return "a" + divide(a-1, z, k);   // cnt가 k보다 크면, 앞에 a를 두고 나머지 알파벳을 조합했을 때 k번째 문자열을 구할 수 있음
    else return "z" + divide(a, z-1, k-cnt);        // cnt가 k보다 작으면, 앞에 z를 두고 나머지를 조합. 이 때 k는 앞에 오는(a로 시작하는) cnt개의 문자열보다 뒤에 있기 때문에 k-cnt로 renumbering됨
}

if (combination(n+m, Math.min(n, m)) < k) console.log("-1"); // a n개와 z m개로 만들 수 있는 문자열이 k개보다 적으면 -1 출력
else console.log(divide(n, m, k));