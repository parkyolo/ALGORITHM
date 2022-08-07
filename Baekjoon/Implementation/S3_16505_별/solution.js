// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const N = +input;

let board = Array.from({ length : 2**N }, () => Array.from({ length : 2**N }, () => ' '));
function star(n, x, y) {
    if (n == 1) {
        board[x][y] = '*';
        return;
    }
    
    let nn = parseInt(n / 2); 
    star(nn, x, y);
    star(nn, x + nn, y); 
    star(nn, x, y + nn);
}

star(2**N, 0, 0);
for (let line of board) {
    console.log(line.join("").trim());
}