#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
string N;

int main() {
    cin >> N;
    vector<int> nums;
    for (int i=0; i<N.size(); i++) { // nums에 N의 자릿수를 숫자로 변환해서 넣음
        nums.push_back((int)N.at(i)-48);
    }

    sort(nums.begin(), nums.end()); // 숫자를 내림차순 정렬
    if (nums[0] != 0) { // 숫자에 0이 없으면 30으로 나누어 떨어지지 않음
        cout << -1;
        return 0;
    }

    long long sum = 0;
    for (int i=1; i<nums.size(); i++) {
        sum += nums[i]; 
    }
    if (sum % 3 > 0) { // 모든 숫자를 더했을 때 3의 배수가 아니면 3으로 나누어 떨어지지 않음
        cout << -1;
        return 0;
    }
    
    // 10이 곱해져 있고 모든 숫자를 더했을 때 3의 배수이면 30으로 나누어 떨어진다.
    string ans = "";
    for (int i=nums.size()-1; i>=0; i--) {
        ans += to_string(nums[i]); // 숫자를 큰 순으로 더했을 때 가장 큰 수가 됨
    }
    cout << ans;
    return 0;
}