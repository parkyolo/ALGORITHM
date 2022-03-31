#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <limits.h>
#define MAX 21
using namespace std;

int N;
int space[MAX][MAX];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int sec = 0; // 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간


void move(int x, int y, int shark, int cnt) { // x좌표, y좌표, 아기 상어의 크기, 잡아 먹은 물고기 수
    space[x][y] = 0;
    if (shark == cnt) { // shark만큼 물고기를 먹으면 shark++
        shark++;
        cnt=0;
        }

    int v[MAX][MAX] = {};
    vector<pair<int,int>> fish;
    queue<pair<int, int>> q;
    
    q.push({x, y});

    while (!q.empty()) { // 먹을 수 있는 물고기 탐색
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int i=0; i<4; i++) {
            int nx = cx+dx[i];
            int ny = cy+dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && v[nx][ny] == 0) {
                if (space[nx][ny] == shark || space[nx][ny] == 0) {
                    v[nx][ny] = v[cx][cy] + 1; // 거리 체크
                    q.push({nx, ny});
                } else if (space[nx][ny] < shark) {
                    v[nx][ny] = v[cx][cy] + 1;
                    fish.push_back({nx, ny});
                    q.push({nx, ny});
                }
            }
        }
    }

    int fx, fy;
    if (fish.size() == 0) return; // 더 이상 먹을 수 있는 물고기가 없을 때
    else if (fish.size() == 1) { // 먹을 수 있는 물고기가 1마리일 때
        fx = fish[0].first;
        fy = fish[0].second;
        sec += v[fx][fy];
        move(fx, fy, shark, cnt+1);
    }
    else { // 먹을 수 있는 물고기가 1마리보다 많을 때
        int min_dist = INT_MAX; // 가장 가까운 거리
        int min_cnt = 0;
        vector<pair<int, int>> minfish;
        for (int i=0; i<fish.size(); i++) {
            int ix = fish[i].first;
            int iy = fish[i].second;
            if (v[ix][iy] < min_dist) {
                min_dist = v[ix][iy];
                fx = ix;
                fy = iy;
                min_cnt = 1;
                minfish.push_back({ix, iy});
            } else if (v[ix][iy] == min_dist) {
                min_cnt++;
                minfish.push_back({ix, iy});
            }
        }

        if (min_cnt > 1) { // 거리가 가까운 물고기가 많을 때
            sort(minfish.begin(), minfish.end()); // 가장 위에, 가장 왼쪽에 있는 물고기를 찾음
            fx = minfish[0].first;
            fy = minfish[0].second;
        }
        sec += min_dist;
        move(fx, fy, shark, cnt+1);
        
    }
}

int main() {
    cin >> N;

    int x, y;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> space[i][j];
            if (space[i][j] == 9) {
                x = i;
                y = j;
            }
        }
    }

    move(x, y, 2, 0);
    cout << sec;
    return 0;
}