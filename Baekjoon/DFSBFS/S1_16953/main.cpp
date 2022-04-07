#include <iostream>
#include <limits.h>
using namespace std;
int A, B;
int ans = INT_MAX;

void MultiorPlus(long n, int cnt) {
    if (n == B) {
        if (cnt < ans) {
            ans = cnt;
            return;
        }
    }
    if (cnt > ans || n > B) return;
    MultiorPlus(n*2, cnt+1);
    MultiorPlus(n*10+1, cnt+1);
}

int main() {
    cin >> A >> B;
    MultiorPlus(A, 0);
    if (ans == INT_MAX) {
        ans = -1;
    } else {
        ans ++;
    }
    cout << ans;
}