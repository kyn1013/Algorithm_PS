#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,number(2);
	int arr[100] = {};
	cin >> n;
	cin >> arr[0];
	arr[0]++;
	for (int i = 1; i < n; i++) {
		int k;
		cin >> k;
		if (k != 0) {
			for (int j = i - 1; j >= i - k; j--) {
				arr[j + 1] = arr[j];
			}
		}
		arr[i - k] = number++;
	}
	for (int i = 0; i < n; i++) cout << arr[i] << " ";
}
