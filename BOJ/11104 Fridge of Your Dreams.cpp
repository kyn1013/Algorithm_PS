#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num(1);
		long long sum(0);
		string number;
		cin >> number;
		for (int i = 23; i >= 0; i--) {
			if (number[i] == '1') {
				sum = sum + num;
			}
			num *= 2;
		}
		cout << sum << "\n";
	}
}
