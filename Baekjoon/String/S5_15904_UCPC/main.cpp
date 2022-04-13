#include <iostream>
using namespace std;
string S;

int main() {
    getline(cin, S); // 공백포함 문자열 입력
    char UCPC[] = {'U', 'C', 'P', 'C'};
    int idx = 0;
    for (int i=0; i<S.length(); i++) {
        if (S.at(i) == UCPC[idx]) {
            idx++;
        }
    }
    if (idx == 4) cout << "I love UCPC";
    else cout << "I hate UCPC";
    return 0;
}