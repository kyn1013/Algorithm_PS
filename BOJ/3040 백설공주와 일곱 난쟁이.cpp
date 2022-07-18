#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[9] = {};
	int sum(0), a(0), b(0);
	for (int i = 0; i < 9; i++) cin >> arr[i];
	for (int i = 0; i < 9; i++) sum += arr[i];
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			int ans(0);
			ans = sum - arr[i] - arr[j];
			if (ans == 100) {
				a = i;
				b = j;
				break;
			}
		}
	}
	for (int i = 0; i < 9; i++) {
		if (i != a && i != b) cout << arr[i]<<"\n";
	}
}
