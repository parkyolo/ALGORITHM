#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;
    int i=0;
    string ans = "";
    while (i<S.length()) {
        if (S[i] == 'X') {
            int start = i; 
            while (i<S.length() && S[i] != '.') { // 연속된 X의 길이 구하기
                i++;
            }
            int end = i; 
            while (start < end) {
                if (end-start >= 4) { // 연속된 X를 AAAA로 덮기
                    ans += "AAAA";
                    start += 4;
                } else if (end-start >= 2) { // 연속된 X를 BB로 덮기
                    ans += "BB";
                    start += 2;
                } else { // AAAA와 BB로 덮을 수 없는 X가 있을 때는 -1 출력
                    cout << -1;
                    return 0;
                }
            }
            
        } else {
            ans += ".";
            i++;
        }
    }
    cout << ans;
    return 0;
}