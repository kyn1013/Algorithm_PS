#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int sum[5][4] = {};
	int scoresum[5] = {};
	int big,number;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> sum[i][j];
			scoresum[i] += sum[i][j];
		}
	}

	big = scoresum[0];
	number = 0;
	for (int i = 1; i < 5; i++) {
		if (big < scoresum[i])big = scoresum[i],number=i;
	}
	cout << number+1 << ' ' << big;
}
