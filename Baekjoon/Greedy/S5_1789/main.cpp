#include <iostream>
#include <cmath>
using namespace std;
long long S;

int main() {
    cin >> S;

    // 1부터 N까지 빼면서 구하는 풀이
    // int N = 0;
    // while (S > 0) {
    //     N ++;
    //     S -= N;  
    // }
    // if (S < 0) N--;
    // cout << N;

    // 1부터 N까지의 합 공식을 이용한 풀이
    long long N = sqrt(S*2);
    while (N*(N+1) > S*2) N--;
    cout << N;
    return 0;
}