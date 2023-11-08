#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int ans(0);
        char a[100] = {}, b[100] = {};
        cin >> a;
        cin >> b;
        for (int i = 0; i < 100; i++) {
            if (a[i] != b[i]) ans++;
        }
        cout << "Hamming distance is " << ans << ".\n";
    }


}
