#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string number;
	cin >> number;
	long long a = (number[0]-'0');
	long long b = (number[1] - '0');
	long long c = (number[2] - '0');
	long long d = (number[3] - '0');
	long long e = (number[4] - '0');
	long long sum(0);

	a = a*a*a*a*a;
	b = b*b*b*b*b;
	c = c*c*c*c*c;
	d = d*d*d*d*d;
	e = e*e*e*e*e;
	sum = a + b + c + d + e;
	cout << sum;
}
