#include <iostream>
#include <vector>

#define MAX 51
using namespace std;

struct FIREBALL {
    int x;
    int y;
    int m;
    int s;
    int d;
};

int N, M, K;
int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
int divd[2][4] = {{0,2,4,6}, {1,3,5,7}};
vector<FIREBALL> Fireball;


void move() {
    vector<FIREBALL> newFireball[MAX][MAX];

    for (int i=0; i<Fireball.size(); i++) { // 파이어볼 이동
        FIREBALL cur = Fireball[i];
        int cx = cur.x;
        int cy = cur.y;
        int mass = cur.m;
        int speed = cur.s;
        int direc = cur.d;

        int nx = (cx + dx[direc]*speed + N*speed)%N;
        int ny = (cy + dy[direc]*speed + N*speed)%N;
        newFireball[nx][ny].push_back({nx, ny, mass, speed, direc}); 
    }
    Fireball = {};

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (newFireball[i][j].size() == 1) {
                Fireball.push_back(newFireball[i][j][0]);
            } else if (newFireball[i][j].size() > 1) { // 파이어볼 나누기
                int mass_sum = 0; // 질량의 합
                int speed_sum = 0; // 속력의 합
                int fireball_cnt = newFireball[i][j].size(); // 파이어볼의 개수
                int eo[] = {0, 0}; // 짝수, 홀수
                for (int k=0; k<fireball_cnt; k++) {
                    FIREBALL cur = newFireball[i][j][k];
                    mass_sum += cur.m;
                    speed_sum += cur.s;
                    eo[cur.d%2] = 1;
                }

                int nm = mass_sum/5;
                if (nm == 0) continue;
                int ns = speed_sum/fireball_cnt;
                int nd = (eo[0]+eo[1]==2) ? 1 : 0;
                for (int k=0; k<4; k++) {
                    Fireball.push_back({i, j, nm, ns, divd[nd][k]});
                }

                // for (int i=0; i<Fireball.size(); i++) {
                //     cout << Fireball[i].x << Fireball[i].y << Fireball[i].m << Fireball[i].s << Fireball[i].d <<endl;
                // }
                // cout << endl;
            }
                
        }
    }
}

int main() {
    cin >> N >> M >> K;
    for (int i=0; i<M; i++) {
        int r, c, m, s, d;
        cin >> r >> c >> m >> s >> d;
        Fireball.push_back({r-1,c-1,m,s,d});
        }

    for (int i=0; i<K; i++) {
        // cout << i << "times" << endl;
        move();
    }

    int ans = 0;
    for (int i=0; i<Fireball.size(); i++) {
        // cout << Fireball[i].x << Fireball[i].y << Fireball[i].m << Fireball[i].s << Fireball[i].d <<endl;
        ans += Fireball[i].m;
    }
    cout << ans;
    return 0;
}