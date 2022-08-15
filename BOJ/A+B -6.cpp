#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0l; i < n; i++) {
        char num[3] = {};
        for (int i = 0; i < 3; i++) cin >> num[i];
        int a = num[0]-'0';
        int b = num[2] - '0';
        cout << a + b<<"\n";
    }
}
