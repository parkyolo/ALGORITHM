#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string str1, str2;
    cin >> str1 >> str2;
    int len1 = str1.length();
    int len2 = str2.length();

    int lcs[len1][len2];
    for (int i=0; i<len1+1; i++) {
        for (int j=0; j<len2+1; j++) {
            lcs[i][j] = 0;
        }
    }

    int ans = 0;
    for (int i=1; i<len1+1; i++) {
        for ( int j=1; j<len2+1; j++) {
            if (str1[i-1] == str2[j-1]) {
                lcs[i][j] = lcs[i-1][j-1] + 1;
                ans = max(ans, lcs[i][j]);
            }
        }
    }
    cout << ans;
}