#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string j,d;
	int jcount(0), dcount(0);
	cin >> j;
	cin >> d;
	for (auto c : j) if (c == 'a') jcount++;
	for (auto c : d) if (c == 'a') dcount++;

	if (jcount >= dcount) cout << "go";
	else cout << "no";
}
