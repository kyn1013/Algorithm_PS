#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int number[3] = {};
	for (int i = 0; i < 3; i++) cin >> number[i];
	sort(number, number + 3);
	cout << number[1];
}
