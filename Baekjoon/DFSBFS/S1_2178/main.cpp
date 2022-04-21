#include <iostream>
#include <queue>
#include <string.h>
using namespace std;
int N, M;
int maze[101][101];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        string S;
        cin >> S;
        for (int j=0; j<M; j++) {
            maze[i][j] = ((int) S[j]) - 48;
        }
    }

    queue<pair<int, int>> queue;
    int v[N][M];
    memset(v, 0, sizeof(v));

    queue.push({0, 0});
    v[0][0] = 1;
    while (!queue.empty()) {
        int x = queue.front().first;
        int y = queue.front().second;
        queue.pop();
        for (int i=0; i<4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M || maze[nx][ny] == 0) continue; // 이동할 수 있는 칸인지
            if (v[nx][ny] > 0) continue; // 이미 방문한 칸인지
            v[nx][ny] = v[x][y] + 1; // 방문 체크 & 이동 횟수
            queue.push({nx, ny});
        }
    }

    cout << v[N-1][M-1];
    return 0;
}