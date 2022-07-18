#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		int ans(0);
		string str;
		char m[10] = { 'a','e','i','o','u','A','E','I','O','U' };
		getline(cin, str); //문자열 공백으로 입력받기
		if (str[0] == '#') break;
		for (auto c : str) {
			for (int i = 0; i < 10; i++) {
				if (c == m[i]) ans++;
			}
		}
		cout << ans<<"\n";
	}
}
