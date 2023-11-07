#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    char arr[8] = {}; //장조를 저장하는 배열
    int acout(0), dcout(0);
    string ascending = "12345678", descending = "87654321";
    for (int i = 0; i < 8; i++) cin >> arr[i];
    for (int i = 0; i < 8; i++) {
        if (ascending[i] == arr[i]) acout++;
        if(descending[i] == arr[i]) dcout++;
    }

    if (acout == 8) cout << "ascending";
    else if (dcout == 8) cout << "descending";
    else cout << "mixed";

}
