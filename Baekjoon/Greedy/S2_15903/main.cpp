#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1001
using namespace std;
int N, M;

int main() {
    cin >> N >> M;
    vector<long long> A;
    for (int i=0; i<N; i++) {
        int ai;
        cin >> ai;
        A.push_back(ai);
    }
    for (int i=0; i<M; i++) {
        sort(A.begin(), A.end());
        long long x = A[0];
        long long y = A[1];
        A[0] = x+y;
        A[1] = x+y;
    }
    long long ans = 0;
    for (int i=0; i<N; i++) {
        ans += A[i];
    }
    cout << ans;
    return 0;
}