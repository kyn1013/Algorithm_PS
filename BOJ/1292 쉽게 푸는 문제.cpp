#include<iostream>
using namespace std;
int main() {
    int arr[1000] = {};
    int a(0), b(0), n(0),ans(0);
    for (int i = 1; n < 1000; i++) {
        for (int j = 0; j < i; j++) {
            if (n == 1000)break;
            arr[n] = i;
            n++;
        }
    }

    cin >> a;
    cin >> b;
    for (int i = a - 1; i < b; i++)ans += arr[i];
    cout << ans;

}
