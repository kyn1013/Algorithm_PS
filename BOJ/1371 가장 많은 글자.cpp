#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int count[26] = {};
	int same[26] = {};
	int c(0);
	for (int i = 0; i < 50; i++) {
		string s;
		getline(cin, s);
		for (int i = 0; i < s.length(); i++) {
			count[s[i] - 'a']++;
		}
	}
	int big = count[0];
	for (int i = 1; i < 26; i++) {
		if (big < count[i]) {
			big = count[i];
		}
	}
	for (int i = 0; i < 26; i++) {
		if (big == count[i]) {
			same[i] = big;
		}
	}

	for (int i = 0; i < 26; i++) {
		if (same[i] == big) {
			cout << char('a' + i);
		}
	}
}
