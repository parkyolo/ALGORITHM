#include <iostream>
#include <cmath>
using namespace std;
int A[500][500];
int cnt = 0;
int d[4][2] = {{0,-1},{1,0},{0,1},{-1,0}}; // 좌하우상
int dm[4][9][2] = {
    {{0,-2},{-1,-1},{1,-1},{-1,0},{1,0},{-2,0},{2,0},{-1,1},{1,1}},
    {{2,0},{1,-1},{1,1},{0,-1},{0,1},{0,-2},{0,2},{-1,-1},{-1,1}},
    {{0,2},{-1,1},{1,1},{-1,0},{1,0},{-2,0},{2,0},{-1,-1},{1,-1}},
    {{-2,0},{-1,-1},{-1,1},{0,-1},{0,1},{0,-2},{0,2},{1,-1},{1,1}}
    };
int alpha[4][2] = {{0,-1},{1,0},{0,1},{-1,0}};
double pct[9] = {0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01};

void tornado(int cx, int cy, int direc, int move, int n, int move_cnt) {
    // 모래의 이동
    for (int i=0; i<move; i++) {
        cx += d[direc][0];
        cy += d[direc][1];
        int total = 0;
        for (int j=0; j<9; j++) {
            if (cx+dm[direc][j][0] < 0 || cx+dm[direc][j][0] >= n || cy+dm[direc][j][1] < 0 || cy+dm[direc][j][1] >= n) {
                cnt += floor(A[cx][cy]*pct[j]);
            } else {
                A[cx+dm[direc][j][0]][cy+dm[direc][j][1]] += floor(A[cx][cy]*pct[j]);
            }
            total += floor(A[cx][cy]*pct[j]);
        }
        if (cx+alpha[direc][0] < 0 || cx+alpha[direc][0] >= n || cy+alpha[direc][1] || cy+alpha[direc][1] >= n) {
            cnt += (A[cx][cy]-total);
        } else {
            A[cx+alpha[direc][0]][cy+alpha[direc][1]] += (A[cx][cy]-total);
        }
    }
    
    if (cx == 0 && cy == 0) return;

    // 방향 전환
    direc = (direc+1)%4;
    if (move == n-1 && direc == 0) {
        tornado(cx, cy, direc, move, n, -1);
        return;
    }
    if (move_cnt == 2) {
        tornado(cx, cy, direc, move+1, n, 1);
    } else {
        tornado(cx, cy, direc, move, n, 2);
    }
    return;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> A[i][j];
        }
    }
    tornado(n/2, n/2, 0, 1, n, 1);
    cout << cnt;
    return 0;
}