#include <iostream>
using namespace std;
int N, M, J;
int loc[21];

int main() {
    cin >> N >> M >> J;
    for (int i=0; i<J; i++) {
        cin >> loc[i];
    }

    int ans = 0;
    pair<int, int> basket = {1, M};
    for (int i=0; i<J; i++) {
        if (loc[i] >= basket.first && loc[i] <= basket.second) continue;
        int move;
        if (loc[i] < basket.first) move = loc[i]-basket.first;
        else move = loc[i]-basket.second;
        ans += abs(move);
        basket.first += move;
        basket.second += move;
    }
    cout << ans;
    return 0;
}