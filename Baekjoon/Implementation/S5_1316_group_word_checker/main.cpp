#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int N;

int checker(string S) {
    int idx = 1;
    char cur = S[0];
    vector<char> v;
    while (idx < S.length()) {
        if (S[idx] != cur) { // 문자가 바뀌었을 때
            if (find(v.begin(), v.end(), S[idx]) == v.end()) { // 처음 등장한 단어일 때
                v.push_back(cur);
                cur = S[idx];
            } else return 0; // 이미 나온 문자일 때 (해당 문자가 연속하지 않음)
        }
        idx++;
    }
    return 1;
}

int main() {
    cin >> N;

    int cnt = 0;
    for (int i=0; i<N; i++) {
        string S;
        cin >> S; // 단어 입력받기
        cnt += checker(S);
    }
    cout << cnt;
    return 0;
}