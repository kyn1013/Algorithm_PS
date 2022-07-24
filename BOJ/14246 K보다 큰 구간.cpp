#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long n,k;
long long ans(0);
long long arr[100001] = {};
long long sumarr[100001] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> arr[i];
	cin >> k;
	for (int i = 1; i <= n; i++) sumarr[i] = sumarr[i - 1] + arr[i];
	for (int i = 1; i <= n; i++) {
		for (int j = i + 1; j <= n; j++) {
			if (sumarr[j] - sumarr[i - 1] > k) ans++;
		}
	}
	for (int i = 1,j=i; i <= n; i++,j++) {
		if (sumarr[j] - sumarr[i - 1] > k) ans++;
	}
	cout << ans;
}
