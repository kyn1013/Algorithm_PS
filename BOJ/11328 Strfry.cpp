#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n(0);
	cin >> n;
	for (int i = 0; i < n;i++) {
		string stl1;
		string stl2;
		int oc1[26] = {}; //문자열 횟수 담음
		int oc2[26] = {};
		string assert = "Possible";
		cin >> stl1 >> stl2;

		for (auto c : stl1) {
			oc1[c - 'a']++;
		}

		for (auto c : stl2) {
			oc2[c - 'a']++;
		}

		for (int i = 0; i < 1000; i++) {
			if (oc1[i] != oc2[i]) {
				assert = "Impossible";
			}
		}
		cout << assert<<"\n";
	}
}
