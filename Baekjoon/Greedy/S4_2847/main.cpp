#include <iostream>
#define MAX 101
using namespace std;
int N;
int scores[MAX];

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> scores[i];
    }

    int ans = 0;
    for (int i=N-1; i>0; i--) {
        if (scores[i] <= scores[i-1]) {
            ans += scores[i-1] - scores[i] + 1;
            scores[i-1] = scores[i] - 1;
        }
    }

    cout << ans;
    return 0;
}