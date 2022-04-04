#include <iostream>
using namespace std;
int N, K;
int COIN[11];

int main() {
    cin >> N >> K;
    for (int i=0; i<N; i++) {
        cin >> COIN[i];
    }

    for (int i=N-1; i>=0; i--) {
        if (COIN[i] <= K) {
            N = i;
            break;
        }
    }

    int ans = 0;
    for (int i=N; i>=0; i--) {
        ans += K/COIN[i];
        K %= COIN[i];
        if (K == 0) break;
    }
    
    cout << ans;
    return 0;
}