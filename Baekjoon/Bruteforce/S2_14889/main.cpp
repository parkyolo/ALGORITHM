#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <limits.h>
using namespace std;

int N;
int S[21][21];
int ans = INT_MAX;

void get_stats(vector<int> teamS, vector<int> teamL) { // 능력치 구하기
    int start = 0;
    int link = 0;

    for (int i=0; i<N/2-1; i++) {
        for (int j=i+1; j<N/2; j++) {
            start += S[teamS[i]][teamS[j]] + S[teamS[j]][teamS[i]];
            link += S[teamL[i]][teamL[j]] + S[teamL[j]][teamL[i]];
        }
    }
    ans = min(ans,abs(start-link)); // 능력치 차이의 최솟값 구하기
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> S[i][j];
        }
    }

    // 팀 조합
    vector<int> permu(N);
    for (int i=N/2; i<N; i++) permu[i] = 1;
    do { 
        vector<int> teamS = {};
        vector<int> teamL = {};
        for (int i=0; i<N; i++) {
            if (permu[i] == 1) teamS.push_back(i);
            else teamL.push_back(i);
        }
        get_stats(teamS, teamL); // 능력치 구하기
    } while (next_permutation(permu.begin(), permu.end()));

    cout << ans;
    return 0;
}