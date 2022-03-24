#include <iostream>
#include <cmath>
using namespace std;
int A[500][500];
int n, cnt = 0;
int d[4][2] = {{0,-1},{1,0},{0,1},{-1,0}}; // 토네이도가 이동하는 순서별 좌표 변화량
double pct[9] = {0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01};
int ds[4][9][2] = { // pct[i]만큼의 모래가 이동하는 위치 변화량
    {{0,-2},{-1,-1},{1,-1},{-1,0},{1,0},{-2,0},{2,0},{-1,1},{1,1}},
    {{2,0},{1,-1},{1,1},{0,-1},{0,1},{0,-2},{0,2},{-1,-1},{-1,1}},
    {{0,2},{-1,1},{1,1},{-1,0},{1,0},{-2,0},{2,0},{-1,-1},{1,-1}},
    {{-2,0},{-1,-1},{-1,1},{0,-1},{0,1},{0,-2},{0,2},{1,-1},{1,1}}
    };
int alpha[4][2] = {{0,-1},{1,0},{0,1},{-1,0}}; // α 위치

void sand_scattering(int x, int y, int direc) { // 모래 흩날리기
    int total = 0;
    for (int j=0; j<9; j++) {
        int nx = x+ds[direc][j][0];
        int ny = y+ds[direc][j][1];
        int sand = floor(A[x][y] * pct[j]);
        if (nx < 0 || nx >= n || ny < 0 || ny >= n) cnt += sand;
        else A[nx][ny] += sand;
        total += sand;
    }

    int nx = x+alpha[direc][0];
    int ny = y+alpha[direc][1];
    if (nx < 0 || nx >= n || ny < 0 || ny >= n) cnt += (A[x][y]-total);
    else A[nx][ny] += (A[x][y]-total);
    A[x][y] = 0;
}

void tornado(int x, int y) { // 토네이도 이동
    int direc = 0;
    int move_cnt = 1;
    while (x != 0 || y != 0) {
        for (int i=0; i<2; i++) { // move_cnt만큼 2번씩 이동
            for (int j=0; j<move_cnt; j++) { // 한 번 움직일 때마다 모래가 흩날림
                x += d[direc][0];
                y += d[direc][1];
                sand_scattering(x, y, direc);
                if (x == 0 && y == 0) { // (0,0)에 도착하면 종료
                    return;
                }
            }
            direc = (direc+1)%4; // 방향 바꾸기
        }
        move_cnt ++; // 이동 횟수 증가
    }
}

int main() {
    cin >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> A[i][j];
        }
    }
    tornado(n/2, n/2);
    cout << cnt;
    return 0;
}