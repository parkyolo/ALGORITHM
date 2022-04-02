#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int i, int j) {
    return j < i;
}

int main() {
    int N;
    cin >> N;

    int A[N], B[N];
    for (int i=0; i<N; i++) cin >> A[i];
    for (int i=0; i<N; i++) cin >> B[i];

    sort(A, A+N);
    sort(B, B+N, compare);

    int S = 0;
    for (int i=0; i<N; i++) {
        S += A[i] * B[i];
    }

    cout << S;
    return 0;
}