#include <iostream>
#include <algorithm>
using namespace std;

int T;

void JumpLog() { // 통나무 건너뛰기
    int N;
    cin >> N;

    int arr[N];
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+N);
    int stand_log[N];
    for (int i=0; i<N/2; i++) {  // 가장 작은 값 2개씩 처음과 끝에 배치
        stand_log[i] = arr[2*i];
        stand_log[N-i-1] = arr[2*i+1];
    }
    if (N%2 == 1) stand_log[N/2] = arr[N-1]; // 가장 큰 값을 가운데에 넣어줌

    int ans = abs(stand_log[N-1]-stand_log[0]);
    for (int i=0; i<N-1; i++) { // 높이 차의 최댓값을 구함
        if (abs(stand_log[i]-stand_log[i+1]) > ans) ans = abs(stand_log[i]-stand_log[i+1]);
    }

    cout << ans << endl;
}

int main() {
    cin >> T;
    for (int i=0; i<T; i++) {
        JumpLog();
    }

    return 0;
}