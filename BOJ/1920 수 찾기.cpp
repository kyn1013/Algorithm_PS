#include <bits/stdc++.h>
using namespace std;
long long N[100000] = {};
long long M[100000] = {};
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long n, m;
	cin >> n;
	for (int i = 0; i < n; i++) cin >> N[i];
	cin >> m;
	for (int i = 0; i < m; i++) cin >> M[i];
	sort(N, N + n);

	
	for (int i = 0; i < m; i++) {
		int check(0);
		int high = n - 1;
		int low(0);
		while (low<=high) {
			int mid = (low + high) / 2;
			if (M[i] > N[mid]) low = mid+1;
			else if (M[i] == N[mid]) {
				cout << "1";
				check = 1;
				break;
			}
			else if (M[i] < N[mid]) high = mid-1;
		}
		if (check == 0) cout << "0";
		cout << "\n";
	}
}
