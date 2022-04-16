#include <iostream>
#define MAX 10001
using namespace std;
int selfNumber[MAX] = {};

int main() {
    for (int i=1; i<MAX; i++) {
        if (selfNumber[i] == 0) { // selfNumber[i]가 0이면 생성자가 없는 셀프 넘버이므로 출력
            cout << i << endl;
        }
        int n = i;
        int dn = n;
        while (n > 0) { // d(n) 구하기
            dn += n%10;
            n /= 10;
        }
        selfNumber[dn] = i; // selfNumber[d(n)]에 생성자를 넣어줌
    }
    return 0;
}