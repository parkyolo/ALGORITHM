#include <iostream>
#include <vector>
using namespace std;

int N, L;
int map[101][101];
int d[] = {-1, 1};
int ans = 0;

bool runway(int road[], int cur, int direc, vector<int> &visit) {
    if (cur+L*d[direc] < 0 || cur+L*d[direc] >= N) return false; // 범위를 벗어날 경우

    int refer = road[cur];
    for (int i=0; i<L; i++) { // 현재 높이보다 1만큼 낮고 경사로가 없는 길이 L칸 있는지 검사
        if (road[cur+d[direc]] == refer-1 && !visit[cur+d[direc]]) {
            visit[cur+d[direc]] = 1;
            cur += d[direc];
        }
        else return false;
    }
    return true;
}

void pass(int road[]) {
    int i=0;
    vector<int> visit(N); // 방문 체크

    while (i<N-1) {
        if (abs(road[i]-road[i+1]) > 1) return; // 높이가 2칸 이상 차이날 경우
        if (road[i] > road[i+1]) { // 내리막
            if (!runway(road, i, 1, visit)) return;
            else i += L-1;
        }
        else if (road[i] < road[i+1]) { // 오르막
            if (!runway(road, i+1, 0, visit)) return;
        }
        i++;
    }
    // for (int i=0; i<N; i++) cout << road[i] << " ";
    // cout << endl;
    ans += 1;
}

int main() {
    cin >> N;
    cin >> L;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> map[i][j];
        }
    }
    // cout << endl;

    for (int i=0; i<N; i++) {
        int road[N];
        for (int j=0; j<N; j++) road[j] = map[i][j]; // 행을 지나갈 수 있는지
        pass(road);

        fill_n(road,N,0);
        for (int j=0; j<N; j++) road[j] = map[j][i]; // 열을 지나갈 수 있는지
        pass(road);
    }
    cout << ans;
    return 0;
}