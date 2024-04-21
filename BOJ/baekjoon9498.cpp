#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a;
	cin >> a;
	if (90 <= a&&a <= 100)cout << "A";
	else if (80 <= a && a<= 89)cout << "B";
	else if (70 <= a && a<= 79)cout << "C";
	else if (60 <= a && a<= 69)cout << "D";
	else cout << "F";
}
