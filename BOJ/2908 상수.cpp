#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int arr1[3] = {};
    int arr2[3] = {};
    int number1(0), number2(0);
    int n1, n2;
 
    cin >> n1;
    cin >> n2;
    for (int i = 0; i <3; i++) {
        arr1[i] = n1 % 10;
        n1 = n1 / 10;
        arr2[i] = n2 % 10;
        n2 = n2 / 10;
   }
    for (int i = 0,j=100; i < 3; i++,j=j/10) {
        number1 += arr1[i] * j;
        number2 += arr2[i] * j;
    }
    if (number1 > number2) cout << number1;
    else cout << number2;
}
