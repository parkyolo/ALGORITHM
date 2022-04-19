#include <iostream>
#include <vector>
using namespace std;
int N;
int tree[100001] = {};

int main() {
    cin >> N;
    int sum = 0; // 사과나무 높이의 합
    for (int i=0; i<N; i++) {
        cin >> tree[i];
        sum += tree[i];
    }

    if (sum % 3 > 0) cout << "NO"; // 2와 1로 sum을 만들 수 없는 경우
    else {
        int cnt1 = sum/3; // 1만큼 성장시키는 물뿌리개 사용 횟수
        int cnt2 = sum/3; // 2만큼 성장시키는 물뿌리개 사용 횟수
        for (int i=0; i<N; i++) {
            // 2 물뿌리개
            if (tree[i]/2 <= cnt2) {
                cnt2 -= tree[i]/2;
                tree[i] %= 2;
            }
            else if (cnt2 > 0) {
                tree[i] -= 2*cnt2;
                cnt2 = 0;
            }
            // 1 물뿌리개
            if (tree[i] <= cnt1) cnt1 -= tree[i];
            else { // 1과 2를 같은 횟수로 사용할 수 없을 때
                cout << "NO";
                return 0;
            }
        }
        cout << "YES";
    }
    return 0;
}