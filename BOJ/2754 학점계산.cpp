#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
long long arr[15000] = {};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string n;
	cin >> n;
	if (n == "A+") cout << 4.3;
	else if (n == "A0") cout << "4.0";
	else if (n == "A-") cout << 3.7;
	else if (n == "B+") cout << 3.3;
	else if (n == "B0") cout << "3.0";
	else if (n == "B-") cout << 2.7;
	else if (n == "C+") cout << 2.3;
	else if (n == "C0") cout << "2.0";
	else if (n == "C-") cout << 1.7;
	else if (n == "D+") cout << 1.3;
	else if (n == "D0") cout << "1.0";
	else if (n == "D-") cout << 0.7;
	else cout << "0.0";

}
