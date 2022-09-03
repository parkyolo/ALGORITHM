const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i=0; i<4; i++) {
    let [x1, y1, p1, q1, x2, y2, p2, q2] = input[i].split(" ").map(Number);
    if (x1 > x2) {
        [x1, y1, p1, q1, x2, y2, p2, q2] = [x2, y2, p2, q2, x1, y1, p1, q1];
    }
    if (p1 == x2 && (y1 == q2 || q1 == y2)) console.log("c"); // 점
    else if (((y1 == q2 || q1 == y2) && (x1 <= x2 && p1 >= x2)) || (p1 == x2 && ((q1 >= y2 && q1 <= q2) || (y1 <= q2 && q1 >= q2)))) console.log("b"); // 선분
    else if (p1 < x2 || q1 < y2 || y1 > q2) console.log("d"); // 공통부분이 없음
    else console.log("a"); // 직사각형
}