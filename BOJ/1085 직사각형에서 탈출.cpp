#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long arr[4] = {};
	for (int i = 0; i < 4; i++)cin >> arr[i];
	arr[2] = arr[2] - arr[0];
	arr[3] = arr[3] - arr[1];
	sort(arr, arr + 4);
	cout << arr[0];
}
