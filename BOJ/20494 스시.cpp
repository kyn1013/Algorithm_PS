#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, ans(0); //손님 수
    int arr[26] = {}; //스시의 종류
    cin >> N;
    for (int i = 0; i < N; i++) {
        string cus;
        cin >> cus;
        for (auto c : cus) {
            arr[int(c) - 65]++;
        }
    }
    for (int i = 0; i < 26; i++) ans += arr[i];
    cout << ans;
}
