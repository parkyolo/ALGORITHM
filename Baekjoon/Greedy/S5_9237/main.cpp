#include <iostream>
#include <algorithm>
using namespace std;
int N;

int main() {
    cin >> N;
    int trees[N];
    for (int i=0; i<N; i++) {
        cin >> trees[i];
    }

    int ans = 0;
    sort(trees, trees+N);
    for (int i=1; i<=N; i++) {
        trees[N-i] += i;
        ans = max(ans, trees[N-i]);
    }
    cout << ans+1;
    return 0;
}