#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long n;
	char save[51] = {};
	cin >> n;
	cin >> save;
	for (int i = 1; i < n; i++) {
		char str[51] = {};
		cin >> str;
		for (int j = 0; j < 50; j++) {
			if (save[j] != str[j]) save[j] = '?';
		}
	}
	cout << save;
}
