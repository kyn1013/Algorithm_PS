#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[100] = {};
	int n, v, count(0);
	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];
	cin >> v;
	for (int i = 0; i < n; i++) {
		if (arr[i] == v) count++;
	}
	cout << count;
}
