#include <iostream>
using namespace std;
int N, M, T;

void bridge(int t) {
    cin >> N >> M;
    long long dp[N][M];

    for (int i=0; i<N; i++) { // 배열 초기화
        for (int j=0; j<M; j++) {
            dp[i][j] = 0;
        }
    }

    for (int j=0; j <= M-N; j++) {
        dp[0][j] = 1;
    }
    
    for (int i=1; i<N; i++) {
        for (int j=i; j<=M-N+i; j++) {
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
        }
    }

    long long sum = 0;
    for (int i=0; i<M; i++) {
        sum += dp[N-1][i];
    }

    cout << sum << endl;
}

int main() 
{
    cin >> T;
    for (int i=0; i<T; i++) {
        bridge(i);
    }
    return 0;
}