#include <iostream>
#include <algorithm>
#include <vector>
#include <limits.h>
using namespace std;

int N;
int operand[101];
int operator_[4]; // +, -, x, /
int max_result = INT_MIN;
int min_result = INT_MAX;

void calcul(int permu[]) {
    int result = operand[0];
    for (int i=0; i<N-1; i++) {
        if (permu[i] == 0) result += operand[i+1];
        else if (permu[i] == 1) result -= operand[i+1];
        else if (permu[i] == 2) result *= operand[i+1];
        else result /= operand[i+1];
    }

    min_result = min(min_result, result);
    max_result = max(max_result, result);
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) cin >> operand[i];
    for (int i=0; i<4; i++) cin >> operator_[i];

    vector<int> v = {};
    for (int i=0; i<4; i++) {
        for (int j=0; j<operator_[i]; j++) {
            v.push_back(i);
        }
    }
    do { // 모든 순열의 최대, 최솟값 계산
        int permu[N-1];
        for (int i=0; i<v.size(); i++) {
            permu[i] = v[i];
        }
        calcul(permu);
    } while(next_permutation(v.begin(), v.end()));

    cout << max_result << endl;
    cout << min_result;
    return 0;
}