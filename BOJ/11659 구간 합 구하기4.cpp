#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N(0), count(0);
	int arr[100000] = {};
	int sumarr[100000] = {};

	cin >> N;
	cin >> count;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	sumarr[0] = arr[0];
	for (int i = 1; i <= N; i++) sumarr[i] = sumarr[i - 1] + arr[i];
	for (int i = 0; i < count; i++) {
		int k, j;
		cin >> k;
		cin >> j;//배열의 원래 인덱스보다 1씩 큼
		if (k == 1 && k!=j) cout << sumarr[j-1];
		else if(k == j)cout << arr[k - 1]; 
		else cout << sumarr[j-1] - sumarr[k-2];
		cout << "\n";
	}
}
