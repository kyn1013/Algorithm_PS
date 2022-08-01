#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[250000] = {};
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
		if (sum > big) {
			big = sum;
		}
	}

	long long bigN2(X - 1), smallN2(0),sum2(0);
	for (int i = 0; i <= bigN2; i++) sum2 += arr[i];
	if (sum2 == big) count++;
	while (bigN2 <= N - 1) {
		sum2 -= arr[smallN2];
		smallN2++;
		bigN2++;
		sum2 += arr[bigN2];
		if (sum2 == big) count++;
	}

	if (big == 0) cout << "SAD";
	else {
		cout << big << "\n";
		cout << count;
	}
}
