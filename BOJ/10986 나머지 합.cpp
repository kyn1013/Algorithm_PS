#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

long long newarr[1001] = {};
long long N(0), M(0),x(0),sum(0);
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long count(0);
	cin >> N;
	cin >> M;

	for (int i = 0; i < N; i++) {
		cin >> x;
		sum += x;
		newarr[sum%M]++;
	}

	for (int i = 0; i <=1000; i++) {
		count += newarr[i] * (newarr[i] - 1) / 2;
	}
	cout << newarr[0]+count;
}
