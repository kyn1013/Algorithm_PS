#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long n, ans(0);
    cin >> n;
    for (long i = 0; i < n; i++) {
        long p, discrimination(0);
        cin >> p;
        if (p == 1) discrimination = 1;
        for (long i = 2; i < p; i++) {
            if (p % i == 0) discrimination = 1;
        }
        if (discrimination == 0) ans++;
    }
    cout << ans;
}
