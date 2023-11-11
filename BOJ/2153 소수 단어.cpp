#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string word;
    int sum(0), ans(0);
    cin >> word;
    for (auto c : word) {
        if(int(c)>=97) sum += int(c) - 96;
        else sum += int(c) - 65 + 27;
    }

    
    for (int i = 2; i < sum; i++) {
        if (sum % i == 0) ans = 1;
    }
    if( ans == 1 ) cout << "It is not a prime word.";
    else cout << "It is a prime word.";
}
