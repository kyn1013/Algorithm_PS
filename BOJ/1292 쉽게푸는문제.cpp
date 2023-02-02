#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[16000] = {};
	int sum[16000] = {};
	int big(0),ans(0).index(0);
	int s1, s2, s3;
	int count(0);
	cin >> s1;
	cin >> s2;
	cin >> s3;
	for (int i = 1; i <= s1; i++) {
		for (int j = 1; j <= s2; j++){
			for (int k = 1; k <= s3; k++) {
				arr[count++] = i + j + k;
			}
		}
	}
	index = s1 * s2 * s3;
	for (int i = 0; i < index; i++) {
		sum[arr[i]]++;
	}
	big = sum[0];
	for (int i = 1; i < 16000; i++) {
		if (big < sum[i]) {
			big = sum[i];
			ans = i;
		}
	}
	cout << ans;
}
