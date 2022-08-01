#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[100000] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long N, X, sum(0), big(0),count(0);
	cin >> N >> X;
	for (int i = 0; i < N; i++) cin >> arr[i];
	long long bigN(X-1), smallN(0);
	for (int i = 0; i <= bigN; i++) sum += arr[i];
	big = sum;
	while (bigN <= N - 1) {
		sum -= arr[smallN];
		smallN++;
		bigN++;
		sum += arr[bigN];
		if (bigN <= N - 1&&sum > big) {
			big = sum;
		}
	}
	cout << big;
}
