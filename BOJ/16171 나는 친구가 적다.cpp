#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string S;
	string K;
	char arr[101] = {};
	int n(0), ans(1), start(0);
	cin >> S;
	cin >> K;
	for (auto c : S) {
		if ('a' <= c && c <= 'z' || 'A' <= c && c <= 'Z'){
			arr[n] = c;
			n++;
		}
	}

	for (int i = 0; i < 101; i++) {
		if (K[0] == arr[i] && K[1] == arr[i + 1]) start = i;

	}
	for (int i = 0; i < K.length(); i++) {
		if (K[i] != arr[start]) ans = 0;
		start++;
	}

	cout << ans;
}
