#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[2000] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long N,sum;
	cin >> N;
	long long count(0);
	for (int i = 0; i < N; i++) cin >> arr[i];
	sort(arr, arr + N, greater<>());
	for (int k = 0; k < N; k++) {
		long i(0), j(N - 1);
		sum = arr[k];
		if (i == k) i++;
		else if (j == k) j--;
		while (i < j) {
			if (arr[i] + arr[j] < sum) {
				j--;
				if (j == k) j--;
			}
			else if (arr[i] + arr[j] > sum) {
				i++;
				if (i == k) i++;
			}
			else {
					count++;
					break;
				}
		}
	}
	cout << count;
}
