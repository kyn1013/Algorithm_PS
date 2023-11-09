#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long  n;
    long long arr[10000] = {};
    arr[0] = 0;
    arr[1] = 1;
    cin >> n;
    for (long long i = 2; i <= n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    cout << arr[n];
}
