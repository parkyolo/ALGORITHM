#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> ShiftRow(vector<vector<int>> rc, int n, int m) {
    vector<vector<int>> temp;
    for (int i=0; i<n; i++) {
        vector<int> line;
        for (int j=0; j<m; j++) {
            line.push_back(rc[(i-1+n)%n][j]);
        }
        temp.push_back(line);
    }
    return temp;
}

vector<vector<int>> Rotate(vector<vector<int>> rc, int n, int m) {
    vector<vector<int>> temp; 
    for (int i=0; i<n; i++) {
        vector<int> line;
        for (int j=0; j<m; j++) {
            line.push_back(rc[i][j]);
        }
        temp.push_back(line);
    }

    // for (int i=0; i<n; i++) {
    //     for (int j=0; j<m; j++) {
    //         cout << temp[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    vector<int> line;
    for (int i=0; i<m-1; i++) line.push_back(rc[0][i]);
    for (int i=0; i<n-1; i++) line.push_back(rc[i][m-1]);
    for (int i=m-1; i>0; i--) line.push_back(rc[n-1][i]);
    for (int i=n-1; i>0; i--) line.push_back(rc[i][0]);

    int idx = 0;
    temp[0][0] = line.back();
    for (int i=1; i<m-1; i++) {
        temp[0][i] = line.front();
        line.erase(line.begin());
    }
    for (int i=0; i<n-1; i++) {
        temp[i][m-1] = line.front();
        line.erase(line.begin());
    }
    for (int i=m-1; i>0; i--) {
        temp[n-1][i] = line.front();
        line.erase(line.begin());
    }
    for (int i=n-1; i>0; i--) {
        temp[i][0] = line.front();
        line.erase(line.begin());
    }
    
    return temp;
}

vector<vector<int>> solution(vector<vector<int>> rc, vector<string> operations) {
    vector<vector<int>> answer;
    int n = rc.size();
    int m = rc[0].size();
    for (int i=0; i<operations.size(); i++) {
        if (operations[i].compare("ShiftRow") == 0) {
            answer = ShiftRow(rc, n, m);
            rc = answer;

            for (int i=0; i<rc.size(); i++) {
                for (int j=0; j<rc[0].size(); j++) {
                    cout << answer[i][j] << " ";
                }
                cout << endl;
            } cout << endl;

        }
        else {
            answer = Rotate(rc, n, m);
            rc = answer;

            for (int i=0; i<rc.size(); i++) {
                for (int j=0; j<rc[0].size(); j++) {
                    cout << answer[i][j] << " ";
                }
                cout << endl;
            } cout << endl;
        }
    }
    
    return answer;
}

int main() {
    // vector<vector<int>> rc = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    // vector<string> operations = {"ShiftRow", "Rotate", "ShiftRow", "Rotate"};
    vector<vector<int>> rc = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<string> operations = {"Rotate", "ShiftRow"};
    vector<vector<int>> answer = solution(rc, operations);
    for (int i=0; i<rc.size(); i++) {
        for (int j=0; j<rc[0].size(); j++) {
            cout << answer[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}