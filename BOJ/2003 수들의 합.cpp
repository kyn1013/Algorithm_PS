#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[10000] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long N;
	long long M;
	long long start(0);
	long long end(0);
	long long sum(0);
	long long count(0);
	cin >> N >> M;
	for (int i = 1; i <= N; i++) cin >> arr[i];
	while (start<=end&&end<=N) {
		if (sum < M) {
			end++;
			sum += arr[end];
		}
		else if (sum > M) {
			start++;
			sum -= arr[start];
		}
		else {
			count++;
			end++;
			sum += arr[end];
		}
	}
	cout << count;
}
