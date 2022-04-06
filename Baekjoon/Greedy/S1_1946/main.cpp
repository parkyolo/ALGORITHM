#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T;

void solution() {
    int n;
    cin >> n;

    vector<pair<int, int>> rank; // 지원자의 서류심사 성적, 면접 성적의 순위
    for (int i=0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        rank.push_back({a, b});
    }

    sort(rank.begin(), rank.end());
    int ans = 1;
    int temp = rank[0].second;
    for (int i=1; i<n; i++)  {
        if (rank[i].second < temp) {
            ans ++;
            temp = rank[i].second;
            if (temp == 1) break;
        }
    }

    cout << ans << endl;
}

int main() {
    cin >> T;
    for (int i=0; i<T; i++) solution();
    return 0;
}