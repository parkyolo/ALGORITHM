#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 22
using namespace std;

int N;
int CLASSROOM[MAX][MAX];
int like_stud[MAX*MAX][4];
int order[MAX*MAX];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void arrangingSeats(int stud) {
    vector<pair<int,int>> favorite; // 좋아하는 학생이 인접한 칸에 가장 많은 칸
    int max_cnt = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (CLASSROOM[i][j] == 0) {
                int like_cnt = 0;
                for (int k=0; k<4; k++) {
                    int nx = i+dx[k];
                    int ny = j+dy[k];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                    if (find(like_stud[stud], like_stud[stud]+4, CLASSROOM[nx][ny]) != like_stud[stud]+4) like_cnt++;
                }
                if (like_cnt > max_cnt) {
                    favorite.clear();
                    max_cnt = like_cnt;
                    favorite.push_back({i,j});
                } else if (like_cnt == max_cnt) {
                    favorite.push_back({i,j});
                }
            }
            
        }
    }

    if (favorite.size() == 1) {
        CLASSROOM[favorite[0].first][favorite[0].second] = stud;
        return;
    }
    vector<pair<int, int>> empty; // 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
    int max_empty_cnt = 0;
    for (int i=0; i<favorite.size(); i++) {
        int x = favorite[i].first;
        int y = favorite[i].second;
        int empty_cnt = 0;
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            if (CLASSROOM[nx][ny] == 0) empty_cnt++;
        }
        if (empty_cnt > max_empty_cnt) {
            empty.clear();
            max_empty_cnt = empty_cnt;
            empty.push_back({x, y});
        } else if (empty_cnt == max_empty_cnt) {
            empty.push_back({x, y});
        }
    }

    sort(empty.begin(), empty.end()); // 행, 열 번호가 가장 작은 칸부터 오름차순 정렬
    CLASSROOM[empty[0].first][empty[0].second] = stud;
    return;
}

int main() {
    cin >> N;
    for (int i=0; i<N*N; i++) {
        cin >> order[i];
        for (int j=0; j<4; j++) {
            cin >> like_stud[order[i]][j];
        }
    }

    CLASSROOM[1][1] = order[0];// 시작 칸은 1,1
    for (int i=1; i<N*N; i++) arrangingSeats(order[i]);

    int ans = 0; // 만족도
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int cnt = 0;
            int stud = CLASSROOM[i][j];
            for (int k=0; k<4; k++) {
                int nx = i+dx[k];
                int ny = j+dy[k];
                if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                if (find(like_stud[stud], like_stud[stud]+4, CLASSROOM[nx][ny]) != like_stud[stud]+4) cnt++;
            }

            if (cnt == 2) ans += 10;
            else if (cnt == 3) ans += 100;
            else if (cnt == 4) ans += 1000;
            else ans += cnt;
        }
    }
    cout << ans;
}