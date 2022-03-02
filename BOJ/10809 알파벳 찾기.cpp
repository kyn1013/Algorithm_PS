#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string s;
	int arr[26] = {},k(0); //알파벳이 나온 위치를 담는 배열
	cin >> s;
	for (int i = 0; i < 26; i++) arr[i] = -1;
	for (auto c : s) {
		if (arr[c - 'a'] == -1) {
			arr[c - 'a'] = k;
			k++;
		}
		else k++;
	}
	for (int i = 0; i < 26; i++) cout << arr[i] << " ";
}
