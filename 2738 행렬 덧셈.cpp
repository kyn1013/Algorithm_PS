#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,m;
	int arrA[100][100] = {};
	int arrB[100][100] = {};
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) cin >> arrA[i][j];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) cin >> arrB[i][j];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) cout << arrA[i][j]+arrB[i][j]<<" ";
		cout << "\n";
	}


}
