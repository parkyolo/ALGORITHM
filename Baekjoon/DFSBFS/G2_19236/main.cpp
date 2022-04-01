#include <iostream>
#include <algorithm>
#define N 4
using namespace std;

int dx[8][2] = {{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1}};
int MAP[N][N]; // 물고기 번호
int FISHDIR[N][N]; // 물고기 방향
int ans = 0;

void move_fish() { // 물고기 이동
    for (int t=1; t<=16; t++) {
        bool v = false;
        for (int i=0; i<N; i++) {
            if (v) break;
            for (int j=0; j<N; j++) {
                if (MAP[i][j] == t) {
                    int turn_cnt = 0; // 회전 횟수
                    while (!v) {
                        int nd = FISHDIR[i][j];
                        int nx = i+dx[nd][0];
                        int ny = j+dx[nd][1];
                        if (nx >= 0 && nx < N && ny >= 0 && ny < N && MAP[nx][ny] != -1) { // 이동할 수 있을 때
                            int cv = MAP[nx][ny];
                            int cd = FISHDIR[nx][ny];
                            MAP[nx][ny] = MAP[i][j];
                            FISHDIR[nx][ny] = FISHDIR[i][j];
                            MAP[i][j] = cv;
                            FISHDIR[i][j] = cd;
                            v = true;
                            break;
                        } else { // 이동할 수 없을 때 45도 회전
                            if (turn_cnt == 8) v = true; // 이동할 수 있는 칸이 없을 때
                            FISHDIR[i][j] = (nd+1)%8;
                            turn_cnt++;
                        }
                    }
                }
            }
        }
    }
}

void move_shark(int x, int y, int nx, int ny, int fish_num) {
    MAP[x][y] = fish_num;
    MAP[nx][ny] = -1;
}

void copy_arr(int origin[][4], int copy[][4]) { // 배열 복사
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            copy[i][j] = origin[i][j];
        }
    }
}

void dfs(int x, int y, int dir, int sum) {
    // 기존 값 저장해놓기    
    int CMAP[N][N];
    int CFISHDIR[N][N];
    copy_arr(MAP, CMAP);
    copy_arr(FISHDIR, CFISHDIR);
    
    // 최댓값 갱신
    ans = max(ans, sum);

    // 물고기 이동
    move_fish(); 
    
    // 상어 이동
    for (int i=1; i<N; i++) {
        int nd = FISHDIR[x][y];
        int nx = x+dx[nd][0]*i;
        int ny = y+dx[nd][1]*i;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (MAP[nx][ny] == 0) continue;
            int fish_num = MAP[nx][ny];
            int fish_dir = FISHDIR[nx][ny];

            move_shark(x, y, nx, ny, 0); // 물고기가 있는 칸으로 이동
            dfs(nx, ny, fish_dir, sum+fish_num);
            move_shark(nx, ny, x, y, fish_num); // 이동하기 전으로 복구
        } else break;
    }

    // 결과 array 반영
    copy_arr(CMAP, MAP);
    copy_arr(CFISHDIR, FISHDIR);
}

int main() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int a, b;
            cin >> a >> b;
            MAP[i][j] = a;
            FISHDIR[i][j] = b-1;
        }
    }

    // (0,0)에 들어가기
    ans += MAP[0][0];
    MAP[0][0] = -1;
    dfs(0,0,FISHDIR[0][0],ans);

    cout << ans;
    return 0;
}