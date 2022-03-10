#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string word;
    int arr[26] = {}; //알파벳이 나온 횟수를 담는 배열
    int sum(0);
    cin >> word;
    for (auto c : word) {
        if (65 <= c && c <= 67) sum += 3;
        else if (68 <= c && c <= 70) sum += 4;
        else if (71 <= c && c <= 73) sum += 5;
        else if (74 <= c && c <= 76) sum += 6;
        else if (77 <= c && c <= 79) sum += 7;
        else if (80 <= c && c <= 83) sum += 8;
        else if (84 <= c && c <= 86) sum += 9;
        else if (87 <= c && c <= 90) sum += 10;
    }
    cout << sum;
}
