#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		char arr[2000] = {};
		string s;
		int a, k(0), b(0);
		cin >> a >> s;
		k = s.length() * a;
		for (auto c : s) {
			for (int i = 0; i < a; i++) {
				arr[b++] = c;
			}
		}
		for (int i = 0; i < k; i++) cout << arr[i];
		cout << "\n";
	}
}
