#include <iostream>
#include <algorithm>
using namespace std;
int N;
int Ropes[100001];

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> Ropes[i];
    }

    int ans = 0;
    sort(Ropes, Ropes+N);
    for (int i=0; i<N; i++) {
        if (Ropes[i]*(N-i) > ans) ans = Ropes[i]*(N-i);
    }
    cout << ans;
    return 0;
}