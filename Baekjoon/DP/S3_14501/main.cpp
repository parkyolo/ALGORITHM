#include <iostream>
#include <algorithm>
using namespace std;

int N;
int T[16];
int P[16];
int dp[16];

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> T[i] >> P[i];
    }
    for (int i=0; i<N; i++) {
        int money = P[i];
        for (int j=0; j<=i; j++) {
            money = max(money, P[i]+dp[j]); 
        }
        if (i+T[i] <= N) dp[i+T[i]] = max(dp[i+T[i]], money); 
    }

    cout << *max_element(dp, dp+N+1);
    return 0;
}