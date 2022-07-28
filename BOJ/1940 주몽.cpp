#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[15001] = {};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long N;
	long long M;
	long long count(0);
	long long i(0);
	cin >> N >> M;
	long long j = N-1;
	for (int i = 0; i < N; i++) cin >> arr[i];
	sort(arr, arr + N);
	while (i<j) {
		if (arr[i]+arr[j] < M) {
			i++;
		}
		else if (arr[i] + arr[j] > M) {
			j--;
		}
		else {
			count++;
			i++;
			j--;
		}
	}
	cout << count;
}
