#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a[7] = {}, b[7] = {}, sum(0), small(0),count(0),bcount(0);
	for (int i = 0; i < 7; i++) {
		cin >> a[i];
	}
	for (int i = 0,k=0; i < 7; i++) {
		if (a[i] % 2 == 1) {
			bcount++;
			b[k] = a[i];
			sum += b[k];
			k++;
		}
	}
	small = b[0];
	for (int i = 1; i < bcount; i++) {
		if (small > b[i]) {
			small = b[i];
		}
	}
	for (int i = 0; i < 7; i++) {
		if (b[i] == 0) count++;
	}
	if (count == 7) cout << -1;
	else {
		cout << sum << "\n";
		cout << small;
	}
}
