#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, sum(0), psum(0), ppsum(0);
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if(i == 1){
            sum = ++psum;
        }
        else if (i == 2) {
            sum = ppsum + psum;  // 0 + 1 , sum = 1
        }
        else {
            ppsum = psum;
            psum = sum;
            sum = ppsum + psum; 
        }
    }
    cout << sum;
}
