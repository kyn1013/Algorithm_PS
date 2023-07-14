#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string n;
	int count(0);
	cin >> n;
	for (char k : n) {
		if (k == 'a' || k == 'e' || k == 'i' || k == 'o' || k == 'u') count++;
	}
	cout << count;
}
