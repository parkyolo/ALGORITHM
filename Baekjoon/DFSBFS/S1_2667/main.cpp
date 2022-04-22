#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int N;
int map_[26][26];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
vector<int> res; // 단지에 속하는 집의 수

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        string S;
        cin >> S;
        for (int j=0; j<N; j++) {
            map_[i][j] = ((int)S[j])-48;
        }
    }

    queue<pair<int,int>> queue;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (map_[i][j] == 1) { // 집이 있는 곳
                queue.push({i, j});
                map_[i][j] = 0; // 방문 체크
                int cnt = 0;
                while (!queue.empty()) { // BFS
                    int x = queue.front().first;
                    int y = queue.front().second;
                    cnt += 1;
                    queue.pop();
                    for (int k = 0; k<4; k++) { // 4방향으로 연결된 집 찾기
                        int nx = x+dx[k];
                        int ny = y+dy[k];
                        if (nx < 0 || nx >= N || ny < 0 || ny >= N || map_[nx][ny] == 0) continue; // 범위를 벗어나거나 집이 없으면 continue
                        queue.push({nx, ny});
                        map_[nx][ny] = 0; // 방문 체크
                    }
                }
                res.push_back(cnt);
            }
        }
    }

    sort(res.begin(), res.end()); // 오름차순 정렬
    cout << res.size() << endl;
    for (int i=0; i<res.size(); i++) {
        cout << res[i] << endl;
    }
    return 0;
}   