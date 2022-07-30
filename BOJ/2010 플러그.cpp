#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[500000] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long N,big,ans(0);
	cin >> N;
	for (int i = 0; i < 500000; i++) arr[i]=1001;
	for (int i = 0; i < N; i++) cin >> arr[i];
	sort(arr, arr + N);
	big = N - 1;

	for (int i = 0; i < N; i++) {
		if (i == 0)ans += arr[big];
		else ans += arr[big] - 1;
		big--;
		if (arr[big] == 1)break;
	}
	cout << ans;
}
