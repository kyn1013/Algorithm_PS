#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long ans(0);
	long long start(0);
	long long end(0);
	long long sum(0);
	long long N;
	cin >> N;
	
	for (; start != N;) {
		if (sum == N) {
			ans++;
			end++;
			sum += end;
		}
		else if (sum > N) {
			start++;
			sum -= start;
		}
		else {
			end++;
			sum += end;
		}
		
	}

	cout << ans;
}
