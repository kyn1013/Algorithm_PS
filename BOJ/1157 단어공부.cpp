#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[59] = {}; //알파벳이 나온 횟수를 카운트하는 배열
	int count(0),big(0);
	char k = 'A';
	char a = {};
	string word;
	cin >> word;
	for (auto c : word) {
		arr[c - 'A']++;
	}
	for (int i = 32; i < 59; i++) {
		arr[i - 32]+=arr[i];
		arr[i] = 0;
	}
	big = arr[0];
	for (int i = 0; i < 26; i++) {
		if (arr[i] > big) {
			big = arr[i];
		}
	}
	for (int i = 0; i <26; k++, i++) {
		if (arr[i] == big) a = k;
	}
	for (int i = 0; i < 26; i++) {
		if (arr[i] == big) count++;
	}
	if (count > 1) cout << "?";
	else cout << a;
}
