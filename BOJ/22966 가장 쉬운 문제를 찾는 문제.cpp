#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n,small(0),index(0);
	string str[4] = {};
	int score[4] = {};
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str[i] >> score[i];
	}
	small = score[0];
	for (int i = 1; i < n; i++) {
		if (small > score[i]) {
			small = score[i];
			index = i;
		}
	}
	cout << str[index];
}
