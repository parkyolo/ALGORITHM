#include <iostream>
#define MAX 1000001
using namespace std;

int N;
int B, C;
int candi[MAX];
long long ans = 0;

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        int c;
        cin >> c;
        candi[i] = c;
    }
    cin >> B >> C;

    for (int i=0; i<N; i++) {
        ans++;
        candi[i] -= B;
        if (candi[i] > 0) {
            ans += candi[i]/C;
            if (candi[i]%C > 0) ans ++;
        }
    }
    cout << ans;
}